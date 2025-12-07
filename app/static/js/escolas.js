    const selectCidade = document.getElementById("cidades");
    const selectEscola = document.getElementById("escola");


    selectCidade.addEventListener("change", function () {

        const cidadeSelecionada = this.value;

        selectEscola.innerHTML = '<option value="">Selecione a Escola</option>';

        if (cidadeSelecionada === "#") {
            selectEscola.disabled = true;
            return;
        }

        selectEscola.disabled = false;

        const lista = dadosEscolas[cidadeSelecionada];

        for (const codigo in lista) {
            const nome = lista[codigo];

            const option = document.createElement("option");
            option.value = `${codigo} - ${nome}`;
            option.textContent = `${codigo} - ${nome}`;

            selectEscola.appendChild(option);
        }
    });
