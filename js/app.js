/**
 * Three Sisters Stories - Content Loader
 * Loads content from JSON files and renders it to the page
 */

// Load content for a sister's page
async function loadSisterContent(sisterName) {
  try {
    const response = await fetch(`content/${sisterName}/content.json`);
    const data = await response.json();

    renderVideos(data.videos || []);
    renderBooks(data.books || []);
    renderJournal(data.journal || []);
    renderDrawings(data.drawings || [], sisterName);
  } catch (error) {
    console.log('Loading content...', error);
    // Show empty states if JSON not found
    renderVideos([]);
    renderBooks([]);
    renderJournal([]);
    renderDrawings([], sisterName);
  }
}

// Render videos section
function renderVideos(videos) {
  const container = document.getElementById('videos-grid');
  if (!container) return;

  if (videos.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <span class="icon">🎥</span>
        <p>Videos coming soon!</p>
      </div>
    `;
    return;
  }

  container.innerHTML = videos.map(video => `
    <div class="video-container">
      <div class="video-wrapper">
        <iframe
          src="https://www.youtube-nocookie.com/embed/${video.youtubeId}"
          title="${video.title}"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen>
        </iframe>
      </div>
      <p class="video-title">${video.title}</p>
      ${video.date ? `<p class="video-date">${video.date}</p>` : ''}
    </div>
  `).join('');
}

// Render books section
function renderBooks(books) {
  const container = document.getElementById('books-list');
  if (!container) return;

  if (books.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <span class="icon">📖</span>
        <p>Book reviews coming soon!</p>
      </div>
    `;
    return;
  }

  const emojis = ['📕', '📗', '📘', '📙', '📓', '📔'];
  container.innerHTML = books.map((book, i) => `
    <div class="book-item">
      <span class="book-emoji">${emojis[i % emojis.length]}</span>
      <div class="book-info">
        <h3>${book.title}</h3>
        <p class="author">by ${book.author}</p>
        ${book.thoughts ? `<p class="thoughts">"${book.thoughts}"</p>` : ''}
      </div>
    </div>
  `).join('');
}

// Render journal entries
function renderJournal(entries) {
  const container = document.getElementById('journal-entries');
  if (!container) return;

  if (entries.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <span class="icon">✏️</span>
        <p>Journal entries coming soon!</p>
      </div>
    `;
    return;
  }

  container.innerHTML = entries.map(entry => `
    <div class="journal-entry">
      <p class="date">${entry.date}</p>
      <div class="content">${formatMarkdown(entry.content)}</div>
    </div>
  `).join('');
}

// Render drawings gallery
function renderDrawings(drawings, sisterName) {
  const container = document.getElementById('drawings-gallery');
  if (!container) return;

  if (drawings.length === 0) {
    container.innerHTML = `
      <div class="empty-state">
        <span class="icon">🖍️</span>
        <p>Drawings coming soon!</p>
      </div>
    `;
    return;
  }

  container.innerHTML = drawings.map(drawing => `
    <div class="drawing-item">
      ${drawing.image
        ? `<img src="images/${sisterName}/${drawing.image}" alt="${drawing.title}">`
        : `<div class="drawing-placeholder">${drawing.emoji || '🎨'}</div>`
      }
      <p class="title">${drawing.title}</p>
    </div>
  `).join('');
}

// Simple markdown formatter (handles basic formatting)
function formatMarkdown(text) {
  if (!text) return '';

  return text
    // Bold
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    // Italic
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    // Line breaks
    .replace(/\n/g, '<br>');
}

// Smooth scroll for anchor links
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});
