const SIZE_CONSTANTS = 50;

class Grid {
    #baseDocumentElement;
    #gridDocumentElement;
    #contentDocumentElement;
    #interactionDocumentElement;

    #ambient = [];
    #weight = [];
    #grid = {};

    #pacman = {
        hidden: true,
        local: null,
        element: null
    }

    #flag = {
        hidden: true,
        local: null,
        element: null
    }

    clickMod = 1;
    groundMod = 1;

    #settings = {
        scale: 1,
        cartesiano_size: 11,
        debuggerOn: false,
    };

    #audio = new Audio('../Public/audio/pacman.mp3');
    #audio2 = new Audio('../Public/audio/finished.mp3');


    constructor(ambient = [], settings = {}, screen) {
        this.#ambient = ambient;

        // this.#weight = weight;

        Object.assign(this.#settings, settings);

        this.Screen = screen;
    }

    createGrid() {
        const root = document.documentElement;

        var base = document.getElementById("base");
        this.#baseDocumentElement = base;

        var content = document.createElement("div");
        content.id = "content";
        this.#contentDocumentElement = content;

        var grid = document.createElement("div");
        grid.id = "grid";
        this.#gridDocumentElement = grid;

        base.appendChild(content);
        base.appendChild(grid);

        const ambient = this.#ambient;

        let { scale, cartesiano_size } = this.#settings;

        let base_size = SIZE_CONSTANTS * scale;

        var pacman = document.createElement("div");
        pacman.classList = "pacman to-left hide";


        var flag = document.createElement("i");
        flag.classList = "ph-fill ph-flag-checkered icon hide";
        flag.style.position = "absolute";
        flag.style.zIndex = "100";

        content.appendChild(pacman);
        content.appendChild(flag);

        this.#pacman.element = pacman;
        this.#flag.element = flag;

        cartesiano_size += 2;

        root.style.setProperty("--size", base_size + "px");
        root.style.setProperty("--size", base_size + "px");

        let full_size = base_size * cartesiano_size;

        grid.style.width = full_size + "px";
        grid.style.height = full_size + "px";

        content.style.width = grid.style.width;
        content.style.height = grid.style.height;

        let x = 0;
        let y = 0;

        for (let i = 1; i <= cartesiano_size; i++) {
            this.#grid[i] = {};

            for (let e = 1; e <= cartesiano_size; e++) {
                let block = document.createElement("div");

                let isActive = ambient.findIndex(
                    (coord) => coord[0] == e && coord[1] == i
                );

                block.classList = `block ${isActive == -1 ? "" : "block-active"}`;
                block.setAttribute("id", `${e}-${i}`);

                block.onclick = (event) => {
                    this.click(event, block, e, i);
                };

                block.style.minHeight = base_size;
                block.style.minWidth = base_size;

                block.style.left = x + "px";
                block.style.top = y + "px";

                let span = document.createElement("span");
                span.className = "coord";
                span.innerHTML = `${e} - ${i}`;

                block.setAttribute("coord", `${e}-${i}`);
                span.setAttribute("coord", `${e}-${i}`);

                grid.appendChild(block);

                x += base_size;

                this.#grid[i][e] = block;
            }

            x = 0;
            y += base_size;
        }

        this.texture();
    }

    texture() {
        let { cartesiano_size } = this.#settings;

        cartesiano_size += 2;

        for (let y = 1; y <= cartesiano_size; y++)
            for (let x = 1; x <= cartesiano_size; x++) {
                [
                    "texture-b-bottom",
                    "texture-b-top",
                    "texture-b-left",
                    "texture-b-right",
                    "texture-b-block",
                    "texture-b-inline",
                    "texture-b-bottom-left",
                    "texture-b-bottom-right",
                    "texture-b-top-left",
                    "texture-b-top-right",
                    "texture-b-all",
                    "texture-b-null",
                    "texture-b-inline-top",
                    "texture-b-inline-bottom",
                    "texture-b-block-right",
                    "texture-b-block-left",
                ].forEach(className => this.#grid[y][x].classList.remove(className));

                if (this.coordIsActive(x, y))
                    this.#grid[y][x].classList.add("texture-floor");
                else {
                    let top = this.coordIsActive(x, y + 1);
                    let bottom = this.coordIsActive(x, y - 1);
                    let left = this.coordIsActive(x - 1, y);
                    let right = this.coordIsActive(x + 1, y);

                    if (top && !bottom && !left && !right)
                        this.#grid[y][x].classList.add("texture-b-bottom");
                    else if (!top && bottom && !left && !right)
                        this.#grid[y][x].classList.add("texture-b-top");
                    else if (!top && !bottom && left && !right)
                        this.#grid[y][x].classList.add("texture-b-left");
                    else if (!top && !bottom && !left && right)
                        this.#grid[y][x].classList.add("texture-b-right");
                    else if (top && bottom && !left && !right)
                        this.#grid[y][x].classList.add("texture-b-block");
                    else if (!top && !bottom && left && right)
                        this.#grid[y][x].classList.add("texture-b-inline");
                    else if (top && !bottom && left && !right)
                        this.#grid[y][x].classList.add("texture-b-bottom-left");
                    else if (top && !bottom && !left && right)
                        this.#grid[y][x].classList.add("texture-b-bottom-right");
                    else if (!top && bottom && left && !right)
                        this.#grid[y][x].classList.add("texture-b-top-left");
                    else if (!top && bottom && !left && right)
                        this.#grid[y][x].classList.add("texture-b-top-right");
                    else if (top && bottom && left && right)
                        this.#grid[y][x].classList.add("texture-b-all");
                    else if (!top && !bottom && !left && !right)
                        this.#grid[y][x].classList.add("texture-b-null");
                    else if (top && !bottom && left && right)
                        this.#grid[y][x].classList.add("texture-b-inline-bottom");
                    else if (!top && bottom && left && right)
                        this.#grid[y][x].classList.add("texture-b-inline-top");
                    else if (top && bottom && !left && right)
                        this.#grid[y][x].classList.add("texture-b-block-right");
                    else
                        this.#grid[y][x].classList.add("texture-b-block-left");
                }
            }
    }

    coordIsActive(x, y) {
        return this.#ambient.findIndex(
            (coord) => coord[0] == x && coord[1] == y
        ) != -1;
    }

    set pacman(local) {
        let gridBlock = this.#grid[local[1]][local[0]];

        let { top, left } = gridBlock.style;

        this.#pacman.hidden = false;
        this.#pacman.element.classList.remove("hide");
        this.#pacman.element.style.top = top;
        this.#pacman.element.style.left = left;

        this.#pacman.local = local;
    }
    get pacman() { return { active: !this.#pacman.hidden, coord: this.#pacman.local.map(number => number - 1).join(",") }; }

    set flag(local) {
        let gridBlock = this.#grid[local[1]][local[0]];

        let { top, left } = gridBlock.style;

        this.#flag.hidden = false;
        this.#flag.element.classList.remove("hide");
        this.#flag.element.style.top = top;
        this.#flag.element.style.left = left;
        this.#flag.element.style.marginTop = "3px";
        this.#flag.element.style.marginLeft = "1px";

        this.#flag.local = local;
    }

    get flag() { return { active: !this.#flag.hidden, coord: this.#flag.local.map(number => number - 1).join(",") }; }

    click(e, element, X, Y) {
        const index = this.#ambient.findIndex(
            (coord) => coord[0] == X && coord[1] == Y
        );

        if (this.clickMod === 1) {
            var weight = -1;

            if (!element.classList.contains("block-active")) {
                this.#ambient.push([X, Y]);

                element.classList.add("block-active");
            } else {
                this.#ambient.splice(index, 1);

                element.classList.remove("block-active");
            }
        } else if (this.clickMod === 2) {
            if (this.coordIsActive(X, Y)) this.pacman = [X, Y];
            else this.Screen.alert("Você não pode adicionar ele em uma parede", "danger");
        } else if (this.clickMod === 3) {
            if (this.coordIsActive(X, Y)) this.flag = [X, Y];
            else this.Screen.alert("Você não pode adicionar uma bandeira em uma parede", "danger");
        }

        this.texture();
    }

    get map() {
        let { cartesiano_size } = this.#settings;

        cartesiano_size += 2;
        let map = "";

        for (let y = 1; y <= cartesiano_size; y++) {
            for (let x = 1; x <= cartesiano_size; x++)
                map += (this.coordIsActive(x, y) ? "1" : "0") + (x === cartesiano_size ? "" : ",");

            map += y === cartesiano_size ? "" : "-";
        }

        return map;
    }



    playSound() {
        this.#audio.loop = true;
        this.#audio.volume = 0.05;
        this.#audio.play();
    }

    stopSound() {
        this.#audio.loop = false;
        this.#audio.pause();
        this.#audio.currentTime = 0;
        this.#audio.volume = 0.05;
    }

playSoundPix() {
        this.#audio2.volume = 0.05;
        this.#audio2.play();
    }


    makePath(path, passCoord = null) {
        let coord = path[0];

        path.splice(0, 1);

        this.pacman = coord;
        if (passCoord != null) {

            let [pC_x, pC_y] = passCoord;
            let [c_x, c_y] = coord;
            let direction;

            if (pC_x == c_x && pC_y > c_y)
                direction = "to-up";
            else if (pC_x > c_x && pC_y == c_y)
                direction = "to-left";
            else if (pC_x < c_x && pC_y == c_y)
                direction = "to-rigth";
            else
                direction = "to-down";

            [
                "to-left",
                "to-rigth",
                "to-up",
                "to-down",
            ].forEach(className => this.#pacman.element.classList.remove(className));
            this.#pacman.element.classList.add(direction);
            this.#pacman.element.classList.add("pacman-eating");
        }
        else this.playSound()

        this.#pacman.element.classList.add("pacman-slow");

        if (path.length != 0)
            setTimeout(() => {
                this.makePath(path, coord);
            }, 950);
        else {

            this.#flag.element.classList.add("hide");
            this.#flag = {
                ...this.#flag,
                hidden: true,
                local: null
            }

            this.Screen.alert("FINISHED!!", "info");
            this.stopSound()

            this.#pacman.element.classList.remove("pacman-slow");
            this.#pacman.element.classList.remove("pacman-eating");

this.playSoundPix();

        }

    }

}