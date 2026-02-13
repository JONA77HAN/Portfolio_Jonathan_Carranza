async function cargarTendencias() {
    const contenedor = document.getElementById('tendencias-meli');
    try {
        // Suponiendo que tu API de Python corre en localhost:8000
        const response = await fetch('http://127.0.0.1:8000/mercado-libre/tendencias/MLA1055');
        const data = await response.json();

        let html = '<ul>';
        data.forEach(item => {
            html += `<li>🔥 ${item.keyword}</li>`;
        });
        html += '</ul>';
        
        contenedor.innerHTML = html;
    } catch (error) {
        contenedor.innerHTML = "<p>Error al conectar con el backend</p>";
    }
}

document.addEventListener('DOMContentLoaded', cargarTendencias);