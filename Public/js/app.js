$(document).ready(function () {

    //<-----------------GRID----------------->
    const Screen = new ScreenManager();

    const Labirinto = new Grid(
        [[2, 12], [2, 11], [15, 5], [14, 5], [2, 2], [3, 2], [3, 3], [3, 4], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [8, 6], [8, 7], [8, 9], [8, 8], [8, 10], [9, 10], [10, 10], [11, 10], [12, 10], [13, 10], [14, 10], [14, 11], [14, 12], [14, 13], [14, 14], [14, 15], [14, 16], [15, 16], [16, 16], [17, 16], [18, 16], [18, 17], [18, 18], [18, 19], [19, 19], [17, 8], [17, 11], [17, 10], [17, 9], [17, 7], [17, 6], [17, 5], [17, 4], [17, 3], [16, 3], [13, 6], [15, 3], [14, 3], [13, 3], [13, 4], [13, 5], [13, 7], [13, 8], [13, 9], [12, 6], [11, 6], [10, 6], [9, 6], [7, 10], [6, 10], [5, 10], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14], [4, 15], [4, 17], [4, 16], [5, 16], [6, 16], [7, 16], [8, 16], [9, 16], [10, 16], [10, 17], [10, 18], [10, 19], [10, 20], [13, 20], [12, 20], [11, 20], [15, 20], [14, 20], [15, 19], [15, 18], [16, 14], [17, 14], [18, 14], [19, 14], [20, 14], [20, 13], [20, 12], [20, 11], [20, 10], [20, 9], [20, 8], [20, 7], [20, 6], [15, 14], [20, 5], [20, 4], [20, 2], [20, 3], [13, 14], [12, 14], [11, 13], [10, 13], [9, 13], [8, 13], [11, 14], [7, 13], [6, 13], [4, 18], [4, 19], [3, 19], [2, 19], [2, 20], [2, 13], [3, 13], [3, 8], [4, 8], [5, 8], [6, 8], [13, 2], [12, 2], [11, 2], [10, 2], [10, 3], [3, 10], [3, 9], [9, 2], [8, 2], [7, 2], [20, 19], [20, 20], [12, 19], [12, 18], [12, 17], [9, 19], [8, 19], [7, 19], [6, 19], [7, 20], [16, 8], [15, 8], [15, 7], [18, 6], [9, 11], [12, 11], [12, 12], [19, 16], [20, 18], [17, 2], [10, 7], [10, 8], [8, 14], [8, 15], [7, 3], [6, 3], [5, 3], [5, 2], [2, 8], [2, 7], [2, 6], [19, 9], [18, 9], [3, 8], [4, 8], [5, 8], [6, 8]],
        { cartesiano_size: 19, scale: 0.5, },
        Screen
    );

    Labirinto.createGrid();

    //<-----------------BUTÃOS----------------->

    var methodText = null;

    $("#config").click(function () {
        $("#option").toggleClass("active");
    });

    $("#start").click(function () {
        $(".contentStart").css("display", "none");
        $("#container").css("display", "block");
        submit()
        setTimeout(function () {
            $("#container").css("display", "none");
            $(".contentStart").css("display", "flex");
        }, 5000);
    });

    $("#pacman").click(function () {
        $("#pacman").toggleClass("btn_active");

        if ($('#pacman').hasClass('btn_active')) {
            $("#flag").removeClass("btn_active");
            Labirinto.clickMod = 2;
        }
        else Labirinto.clickMod = 1;
    });

    $("#flag").click(function () {
        $("#flag").toggleClass("btn_active");

        if ($('#flag').hasClass('btn_active')) {
            $("#pacman").removeClass("btn_active");
            Labirinto.clickMod = 3;
        }
        else Labirinto.clickMod = 1;
    });

    $(".method_option").click(function () {
        methodText = $(this).find('span').text();
        $("#typeMethod").text(methodText);
    });

    function construirURLComParametros(url, parametros) {
        var partes = [];
        for (var chave in parametros) {
            if (parametros.hasOwnProperty(chave)) {
                partes.push(
                    encodeURIComponent(chave) + "=" + encodeURIComponent(parametros[chave])
                );
            }
        }
        return url + "?" + partes.join("&");
    }

    function submit() {
        if (methodText === null)
            Screen.alert(
                "Selecione um algoritimo",
                "warning"
            )
        else if (!Labirinto.pacman.active)
            Screen.alert(
                "Adicione o Pacman no labirinto.",
                "warning"
            );
        else if (!Labirinto.flag.active)
            Screen.alert(
                "Adicione uma flag no Labirinto.",
                "warning"
            );
        else {

            // const limited_depth = document.getElementById("limited-depth").value ?? 1;

            var xhr = new XMLHttpRequest();

            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    if (xhr.responseText == "error")
                        Screen.alert("Caminho não encontrado", "danger");
                    else {
                        var path;
                        var limite =null;

                        if (methodText == "Aprofundamento Iterativo")
                            [path, limite] = JSON.parse(xhr.responseText);
                        else
                            path = JSON.parse(xhr.responseText);

                        path = path.map(coord => ([coord[1] + 1, coord[0] + 1]));

                        // console.log("Origem: ", Labirinto.pacman.coord);
                        // console.log("Destino: ", Labirinto.flag.coord);
                        // console.log("Caminho: ", path);
                        // console.log("\n\n\n");

                        $('#startOrigin').text("[" + Labirinto.pacman.coord + "]");
                        $('#endOrigin').text("[" + Labirinto.flag.coord + "]");
                        $('#cost').text(path.length);
                        $('#limit').text(limite??0);

                        var array = path

                        var ul = $('#path ul');
                        ul.empty();

                        let subpaths = [];

                        for (let i = 0; i < path.length; i += 4) {
                            subpaths.push(path.slice(i, i + 4));
                        }

                        subpaths.forEach(subpath => ul.append('<li>' + subpath.map(_path => ` [${_path.map(num => num < 10 ? "0" + num : num.toString()).toString()}]`).toString() + '</li>'))

                        Screen.alert("Caminho encontrado", "success");
                        Labirinto.makePath(path);
                    }
                }
            };

            let route = "";

            switch (methodText) {
                case "Amplitude": route = "amplitude"; parametros = { mapa: Labirinto.map, inicio: Labirinto.pacman.coord, fim: Labirinto.flag.coord }; break;
                case "Profundidade": route = "profundidade"; parametros = { mapa: Labirinto.map, inicio: Labirinto.pacman.coord, fim: Labirinto.flag.coord }; break;
                case "Profundidade Limitada": route = "profLimitada"; parametros = { mapa: Labirinto.map, inicio: Labirinto.pacman.coord, fim: Labirinto.flag.coord, limite: $("#ipt_profLim").val() }; break;
                case "Aprofundamento Iterativo": route = "aprofInterativo"; parametros = { mapa: Labirinto.map, inicio: Labirinto.pacman.coord, fim: Labirinto.flag.coord }; break;
                case "Bidirecional": route = "bidirecional"; parametros = { mapa: Labirinto.map, inicio: Labirinto.pacman.coord, fim: Labirinto.flag.coord }; break;
            }

            // if (radio == "profundidadelimit") radio = "/profundidade/" + limited_depth;
            // else if (
            //     radio == "custo_uniforme" ||
            //     radio == "greedy" ||
            //     radio == "aestrela" ||
            //     radio == "aiaestrela"
            // )
            //     parametros = {
            //         ambient: Labirinto.getAmbient(),
            //         weights: Labirinto.getAmbientWeights(),
            //         beginning: cards[0][1],
            //         destination: cards[1][1],
            //     };
            // else
            //     parametros = {
            //         ambient: Labirinto.getAmbient(),
            //         beginning: cards[0][1],
            //         destination: cards[1][1],
            //     };

            xhr.open("GET", construirURLComParametros(`./${route}`, parametros), true);

            xhr.send();
        }
    }

});