document.addEventListener('DOMContentLoaded', () => {
    const gridContainer = document.getElementById('grid-container');
    const scoreValue = document.getElementById('score-value');
    const resetButton = document.getElementById('reset-button');

    let grid = [];
    let score = 0;

    function initializeGrid() {
        grid = Array.from({ length: 4 }, () => Array(4).fill(0));
        addNewTile();
        addNewTile();
        updateGrid();
    }

    function updateGrid() {
        gridContainer.innerHTML = '';
        grid.forEach(row => {
            row.forEach(num => {
                const tile = document.createElement('div');
                tile.className = 'tile';
                tile.textContent = num ? num : '';
                tile.style.backgroundColor = getTileColor(num);
                gridContainer.appendChild(tile);
            });
        });
        scoreValue.textContent = score;
    }

    function addNewTile() {
        const availableCells = [];
        grid.forEach((row, rowIndex) => {
            row.forEach((cell, colIndex) => {
                if (cell === 0) {
                    availableCells.push({ rowIndex, colIndex });
                }
            });
        });

        if (availableCells.length > 0) {
            const { rowIndex, colIndex } = availableCells[Math.floor(Math.random() * availableCells.length)];
            grid[rowIndex][colIndex] = Math.random() < 0.9 ? 2 : 4;
        }
    }

    function getTileColor(value) {
        switch (value) {
            case 2: return '#66c2ff';
            case 4: return '#4db8ff';
            case 8: return '#33adff';
            case 16: return '#1aa3ff';
            case 32: return ' #0099ff';
            case 64: return '#008ae6';
            case 128: return '#007acc';
            case 256: return '#006bb3';
            case 512: return '#005c99';
            case 1024: return '#004d80';
            case 2048: return '#003d66';
            default: return '#ffffff';
        }
    }

    function handleKeyPress(event) {
        const key = event.key;
        let moved = false;

        switch (key) {
            case 'ArrowUp':
                moved = moveUp();
                break;
            case 'ArrowDown':
                moved = moveDown();
                break;
            case 'ArrowLeft':
                moved = moveLeft();
                break;
            case 'ArrowRight':
                moved = moveRight();
                break;
        }

        if (moved) {
            addNewTile();
            updateGrid();
        }
    }

    function moveUp() {
        // Implement move logic for Up direction
        return true; // Replace with actual logic
    }

    function moveDown() {
        // Implement move logic for Down direction
        return true; // Replace with actual logic
    }

    function moveLeft() {
        // Implement move logic for Left direction
        return true; // Replace with actual logic
    }

    function moveRight() {
        // Implement move logic for Right direction
        return true; // Replace with actual logic
    }

    resetButton.addEventListener('click', initializeGrid);
    document.addEventListener('keydown', handleKeyPress);

    initializeGrid();
});

