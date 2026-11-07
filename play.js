import { EMULATOR } from "./emulator_wrapper.js";
import { STATUS_BAR } from './status_bar.js';

// Set the game to my game
const game = "ThumbyBattle";
const startGameBtn = document.getElementById("start-game-btn");

const statusBar = new STATUS_BAR();
statusBar.registerCount(5);

// React stub container mocking GoldernLayout for compatibility
class Container {
  setState(state) { this.state = state; }
  setTitle(title) {}
  focus() {}
}
const conta = new Container();
conta.element = document.body;
const hidden = document.createElement("div");
hidden.style.display = 'none';
conta._layoutManager = hidden;
conta._layoutManager.on = (a, b) => {};

statusBar.loaded(1, "Container Initialized");

// Start warming up the emulator
var EDITORS = [];
var MAIN_EDITOR = null;
var GAME_EDITOR = null;
const emu = await new EMULATOR(conta, {}, EDITORS, statusBar);

statusBar.loaded(1, "Emulator Initialized");

const starter = async () => {
    if (MAIN_EDITOR && GAME_EDITOR) {
        GAME_EDITOR.state.mainChecked = false;
        GAME_EDITOR.MAIN_EMU_CHECKBOX.checked = false;
        MAIN_EDITOR.state.mainChecked = true;
        MAIN_EDITOR.MAIN_EMU_CHECKBOX.checked = true;
    }
    statusBar.showStatusBar();
    await emu.startEmulator();
}
startGameBtn.addEventListener("click", () => {
    starter();
});
//starter();
//emu.EMULATOR_START_BTN.onclick = starter

// On python print, log to console for debugging
emu.onData = async (data) => {
    console.log(data);
    if (data.includes("LOADED_COMPLETE")) {
        statusBar.startGame();
    } else if (data.includes("LOADED")) {
        data = data.replace("LOADED: ", "");
        statusBar.loaded(1, data);
    }
};

// Setup up delaying audio until after unmute
const muter = () => {
  if(emu.EMULATOR_MUTED == undefined || emu.EMULATOR_MUTED == false){
    emu.EMULATOR_MUTED = true;
    emu.EMULATOR_MUTE_BTN.innerHTML = "UNMUTE";
    if (emu.AUDIO_VOLUME != undefined) emu.AUDIO_VOLUME.gain.value = 0.0;
  }else{
    emu.AUDIO_CONTEXT = new(window.AudioContext || window.webkitAudioContext)();

    emu.AUDIO_VOLUME = emu.AUDIO_CONTEXT.createGain();
    emu.AUDIO_VOLUME.connect(emu.AUDIO_CONTEXT.destination);

    emu.AUDIO_BUZZER = emu.AUDIO_CONTEXT.createOscillator();
    emu.AUDIO_BUZZER.frequency.value = 0;
    emu.AUDIO_BUZZER.type = "triangle";
    emu.AUDIO_BUZZER.start();
    emu.AUDIO_BUZZER.connect(emu.AUDIO_VOLUME);

    emu.EMULATOR_MUTED = false;
    emu.EMULATOR_MUTE_BTN.innerHTML = "MUTE";
    emu.AUDIO_VOLUME.gain.value = 0.25;
  }
};

//emu.EMULATOR_MUTE_BTN.onclick = muter;

// Hide unused elements
//emu.EMULATOR_ZOOM_IN_BTN.style.display = 'none';
//emu.EMULATOR_ZOOM_OUT_BTN.style.display = 'none';
//emu.EMULATOR_SCALE_DISPLAY.style.display = 'none';
//emu.EMULATOR_ROTATE_BTN.style.display = 'none';
//emu.EMULATOR_FS_TOGGLE_BTN.style.display = 'none';
//emu.EMULATOR_SCALE_DISPLAY.style.display = 'none';

// Layout
const sizer = () => {
    emu.EMULATOR_THUMBY.style.height = "95%";
    emu.EMULATOR_THUMBY.style.width = "auto";
    emu.EMULATOR_THUMBY.style.left = `${(emu.EMULATOR_BODY_DIV.clientWidth-emu.EMULATOR_THUMBY.clientWidth)/2}px`;
    emu.EMULATOR_CANVAS.style.width = "100%";
    emu.EMULATOR_CANVAS.style.height = "100%";
    const scale = (emu.EMULATOR_BODY_DIV.clientHeight/emu.HEIGHT)*0.1771;
    emu.EMULATOR_CANVAS.width = emu.WIDTH * scale;
    emu.EMULATOR_CANVAS.height = emu.HEIGHT * scale;
    emu.context.translate(emu.WIDTH*scale/2, emu.HEIGHT*scale/2);
    emu.EMULATOR_CANVAS.style.marginTop = '15.6%';
    emu.EMULATOR_CANVAS.style.width = emu.EMULATOR_CANVAS.width + "px";
    emu.EMULATOR_CANVAS.style.height = emu.EMULATOR_CANVAS.height + "px";
    emu.context.scale(scale, scale);
    emu.context.imageSmoothingEnabled = false;
    emu.context.mozImageSmoothingEnabled = false;
    emu.context.oImageSmoothingEnabled = false;
    emu.context.webkitImageSmoothingEnabled = false;
    emu.context.msImageSmoothingEnabled = false;
};
document.addEventListener("DOMContentLoaded", sizer);
emu.adjustSize = sizer;
emu.adjustCanvas = sizer;
sizer();

statusBar.loaded(1);

// Touch screen controls
window.addEventListener("touchstart", (e) => {
    for (let i = 0; i < e.changedTouches.length; i++) {
        switch(e.changedTouches[i].target){
            case emu.EMULATOR_STOP_BTN:
                emu.EMULATOR_STOP_BTN.triggerHandler("click");
                break;
            case emu.EMULATOR_START_BTN:
                emu.EMULATOR_START_BTN.triggerHandler("click");
                break;
            case emu.EMULATOR_MUTE_BTN:
                emu.EMULATOR_MUTE_BTN.triggerHandler("click");
                break;
            case emu.EMULATOR_A_BTN:
                emu.handleKeyDown({key:'.'});
                break;
            case emu.EMULATOR_B_BTN:
                emu.handleKeyDown({key:','});
                break;
            case emu.EMULATOR_DPAD_UP_BTN:
                emu.handleKeyDown({key:'w'});
                break;
            case emu.EMULATOR_DPAD_DOWN_BTN:
                emu.handleKeyDown({key:'s'});
                break;
            case emu.EMULATOR_DPAD_LEFT_BTN:
                emu.handleKeyDown({key:'a'});
                break;
            case emu.EMULATOR_DPAD_RIGHT_BTN:
                emu.handleKeyDown({key:'d'});
                break;
        }
    }
    e.preventDefault();
},{passive: false});
window.addEventListener("touchend", (e) => {
    for (let i = 0; i < e.changedTouches.length; i++) {
        switch(e.changedTouches[i].target){
            case emu.EMULATOR_A_BTN:
                emu.handleKeyUp({key:'.'});
                break;
            case emu.EMULATOR_B_BTN:
                emu.handleKeyUp({key:','});
                break;
            case emu.EMULATOR_DPAD_UP_BTN:
                emu.handleKeyUp({key:'w'});
                break;
            case emu.EMULATOR_DPAD_DOWN_BTN:
                emu.handleKeyUp({key:'s'});
                break;
            case emu.EMULATOR_DPAD_LEFT_BTN:
                emu.handleKeyUp({key:'a'});
                break;
            case emu.EMULATOR_DPAD_RIGHT_BTN:
                emu.handleKeyUp({key:'d'});
                break;
        }
    }
});

const loadGameFiles = async (gameName) => {
    let GameFileURLS = [];
    await fetch("GameManifest.txt")
        .then(response => response.text())
        .then(data => {
            GameFileURLS = data.split(/\r?\n/).filter(line => line.trim() !== "");
        });
    
    // Loop through each URL for this open
    for(let i=0; i<GameFileURLS.length; i++){
        // Added: Make URL and path to my game files
        var fileURL = gameName + "/" + GameFileURLS[i];
        var filePath = "Games/" + fileURL;

        // Get the file contents
        await fetch(fileURL).then(async (response) => {
            // Pass the file contents to the new editor using the state
            var state = {};
            state.value = Array.from(new Uint8Array(await response.arrayBuffer()));
            state.path = filePath;

            // Ensure no collisions with normal editors or cached data
            state.id = `PlayerEditor${i}`;
            (new EditorWrapper(conta, state, EDITORS)).clearStorage();

            // When games are opened, check the boxes so emulation can happen right away
            if(filePath.indexOf(gameName + ".py") != -1){
                state.mainChecked = true;
            }else{
                state.normalChecked = true;
            }

            const edi = new EditorWrapper(conta, state, EDITORS);
            if (state.mainChecked) {GAME_EDITOR = edi}

            console.log(`Loaded file: ${filePath}`);
        });
        statusBar.loaded(1);
    }

    console.log(`Game ${gameName} loaded!`);
}

window.addEventListener('keydown', async (event) =>  {
  if (event.shiftKey && event.key.toLowerCase() === 'q') {
    statusBar.loadingGame();
    loadGameFiles(game);
    emu.restartEmulator();
  }
});


conta.element = hidden;
await loadGameFiles(game);
statusBar.readyToStartGame();