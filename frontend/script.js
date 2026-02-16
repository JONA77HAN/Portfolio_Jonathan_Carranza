async function fetchMeliData() {
    const container = document.getElementById('tendencias-meli');
    const url = 'https://portfolio-backend-jonathan-carranza.onrender.com/mercado-libre/tendencias/MLA1055';

    try {
        const response = await fetch(url);
        const data = await response.json();
        
        // Verificamos si data es realmente una lista (Array)
        if (!Array.isArray(data)) {
            throw new Error("El backend no devolvió una lista de productos");
        }

        container.innerHTML = data.slice(0, 3).map(item => `
            <div class="bg-slate-900/50 p-6 rounded-xl text-center border border-slate-700 hover:border-yellow-400 transition duration-300">
                <p class="text-yellow-400 text-[10px] font-bold tracking-[0.2em] mb-2 uppercase">Tendencia MeLi</p>
                <p class="text-white font-semibold text-lg">${item.keyword}</p>
            </div>
        `).join('');

    } catch (error) {
        console.error("Error detallado:", error);
        container.innerHTML = `
            <div class="col-span-full p-6 text-center bg-red-900/20 border border-red-900/50 rounded-xl">
                <p class="text-red-400 font-mono text-sm italic">
                    Backend conectado pero sin datos: Verifica que la ruta /mercado-libre/tendencias/MLA1055 funcione.
                </p>
            </div>`;
    }
}