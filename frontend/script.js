async function cargarTendencias() {
    const contenedor = document.getElementById('tendencias-meli');
    if (!contenedor) return;

    contenedor.innerHTML = "<li>Cargando tendencias...</li>";

    try {
        console.log("Intentando conectar al backend...");
        const response = await fetch('https://portfolio-backend-jonathan-carranza.onrender.com/mercado-libre/tendencias/MLA1055');
        
        const data = await response.json();
        console.log("¡Datos recibidos con éxito!", data);

        if (data.error) {
            contenedor.innerHTML = `<li>Error: ${data.error}</li>`;
            return;
        }

        let html = '';
        data.forEach(item => {
            html += `<li class="p-2 border-b border-gray-700 text-yellow-400">🔥 ${item.keyword}</li>`;
        });
        
        contenedor.innerHTML = html;

    } catch (error) {
        console.error("Error detallado:", error);
        contenedor.innerHTML = "<li>Error al conectar con el backend. Revisa la consola (F12).</li>";
    }
}

// Asegurémonos de que se ejecute
document.addEventListener('DOMContentLoaded', cargarTendencias);