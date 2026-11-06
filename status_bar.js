export class STATUS_BAR {
    constructor() {
        this.centerWrapper = document.getElementById("center-wrapper");
        this.statusBar = document.getElementById("status-bar");
        this.statusText = document.querySelector(".status-text");
        this.statusFill = document.querySelector(".status-bar-fill");
        this.startGameBtn = document.getElementById("start-game-btn");
        this.background = document.getElementById("background");

        this.totalFiles = 0;
        this.currentFileIndex = 0;
        this.updateStatusBar();
    }
    
    updateStatusBar() {
        this.statusText.textContent = `Files ${this.currentFileIndex}/${this.totalFiles}`;
        this.statusFill.style.width = `${(this.currentFileIndex/this.totalFiles)*100}%`;
    }

    registerCount(count) {
        this.totalFiles += count;
        this.updateStatusBar();
    }

    loaded(count) {
        this.currentFileIndex += count;
        this.updateStatusBar();
    }


    readyToStartGame() {
        this.totalFiles = 0;
        this.currentFileIndex = 0;
        this.statusBar.style.display = "none";
        this.startGameBtn.style.display = "flex";
    }

    showStatusBar() {
        this.statusBar.style.display = "flex";
        this.startGameBtn.style.display = "none";
    }

    startGame() {
        this.centerWrapper.style.display = "none";
        this.background.style.display = "none";
    }
}