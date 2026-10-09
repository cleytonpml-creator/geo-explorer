const filterSelect = document.querySelector('#filtro');
const listContainer = document.querySelector('#lista-trilhas');

async function carregarTrilhas() {
  try {
    const response = await fetch('./data/trilhas.json');
    if (!response.ok) {
      throw new Error('Não foi possível carregar os dados das trilhas.');
    }

    const trilhas = await response.json();
    renderTrilhas(trilhas);
    filterSelect.addEventListener('change', (event) => {
      const dificuldade = event.target.value;
      const filtradas = dificuldade === 'todas'
        ? trilhas
        : trilhas.filter((trilha) => trilha.dificuldade === dificuldade);
      renderTrilhas(filtradas);
    });
  } catch (error) {
    listContainer.innerHTML = `
      <div class="empty-state">
        <p>${error.message}</p>
      </div>
    `;
  }
}

function renderTrilhas(trilhas) {
  if (!trilhas.length) {
    listContainer.innerHTML = `
      <div class="empty-state">
        <p>Nenhuma trilha encontrada para esse filtro.</p>
      </div>
    `;
    return;
  }

  listContainer.innerHTML = trilhas
    .map(
      (trilha) => `
        <article class="card">
          <div class="card-badge">${trilha.dificuldade}</div>
          <h3>${trilha.nome}</h3>
          <p class="meta">${trilha.regiao}</p>
          <p class="description">${trilha.descricao}</p>
          <ul class="details">
            <li><strong>Distância:</strong> ${trilha.distancia}</li>
            <li><strong>Tempo:</strong> ${trilha.tempo}</li>
            <li><strong>Tipo:</strong> ${trilha.tipo}</li>
          </ul>
          <div class="coords">
            <span>📍 ${trilha.coordenadas[0]}, ${trilha.coordenadas[1]}</span>
          </div>
        </article>
      `,
    )
    .join('');
}

carregarTrilhas();
