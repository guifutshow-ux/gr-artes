# Rotina diária: Boletim Tech GR

Um story por dia (seg a sáb) com uma novidade de tecnologia/Apple.

1. Pesquisar uma novidade das últimas 24-48h em fonte oficial ou grande veículo
   (Apple Newsroom, MacRumors, 9to5Mac, The Verge, Reuters, Tecnoblog, Canaltech).
   Só fatos confirmados. Nada de preço, GB, cor, bateria ou garantia de produto da loja.
   Não repetir tema dos boletins anteriores (ver pasta 2026-*/educativos/boletim_*).
2. Escrever dados.json (ver cabeçalho do boletim.py): título curto, subtítulo, 3 ou 4 fatos curtos, fonte.
3. `python3 boletim.py dados.json && node shot.js <slug>` e converter para JPG (qualidade 92).
4. Conferir a imagem (texto não pode vazar do card nem encostar no rodapé).
5. Salvar em `<AAAA-MM>/educativos/boletim_<AAAA-MM-DD>_<tema>.jpg`, commit e push no branch claude/project-thread-q8kzg3.
6. Agendar story no Metricool (blogId 7713533, Instagram, tipo STORY) com a URL raw do GitHub:
   13:00 em dias úteis; 12:30 sábados e feriados. Sem stories no domingo.
