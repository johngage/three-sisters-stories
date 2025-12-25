# Three Sisters Stories

A simple, colorful website for Susie (9), Betsy (7), and Natalie (5) to share their videos, books, journal entries, and drawings.

**No build tools required!** Just plain HTML, CSS, and JavaScript.

## Quick Start

### Local Preview

```bash
# Using Python (built into macOS)
cd three-sisters-stories
python3 -m http.server 8000

# Then open http://localhost:8000
```

### Deploy to GitHub Pages

1. Create a new repository on GitHub named `three-sisters-stories.github.io`

2. Push this code:
   ```bash
   cd three-sisters-stories
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/three-sisters-stories.github.io.git
   git push -u origin main
   ```

3. Go to Settings → Pages → Source: "Deploy from a branch" → Branch: `main`

4. Your site will be live at `https://YOUR_USERNAME.github.io/three-sisters-stories.github.io`

## Adding Content

Edit the JSON files in the `content/` folder:

### Videos

Edit `content/[sister]/content.json`:

```json
{
  "videos": [
    {
      "youtubeId": "dQw4w9WgXcQ",
      "title": "My Dance Video",
      "date": "December 2024"
    }
  ]
}
```

**Getting YouTube Video ID:**
- URL: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- Video ID: `dQw4w9WgXcQ` (the part after `v=`)

### Books

```json
{
  "books": [
    {
      "title": "Book Title",
      "author": "Author Name",
      "thoughts": "What I thought about it!"
    }
  ]
}
```

### Journal Entries

```json
{
  "journal": [
    {
      "date": "December 25, 2024",
      "content": "Today was amazing! We went to the park and I saw a butterfly."
    }
  ]
}
```

### Drawings

**Option 1: Use emoji placeholders**
```json
{
  "drawings": [
    {
      "title": "My Rainbow",
      "emoji": "🌈"
    }
  ]
}
```

**Option 2: Upload actual images**
1. Save image to `images/[sister]/drawing.jpg`
2. Reference in JSON:
```json
{
  "drawings": [
    {
      "title": "My Rainbow",
      "image": "drawing.jpg"
    }
  ]
}
```

## File Structure

```
three-sisters-stories/
├── index.html          # Homepage
├── susie.html          # Susie's page
├── betsy.html          # Betsy's page
├── natalie.html        # Natalie's page
├── css/
│   └── style.css       # All styles
├── js/
│   └── app.js          # Content loader
├── content/
│   ├── susie/
│   │   └── content.json
│   ├── betsy/
│   │   └── content.json
│   └── natalie/
│       └── content.json
└── images/
    ├── susie/          # Susie's drawings
    ├── betsy/          # Betsy's drawings
    └── natalie/        # Natalie's drawings
```

## Customization

### Colors

Edit the CSS variables in `css/style.css`:

```css
:root {
  --susie-color: #FF6B9D;    /* Pink */
  --betsy-color: #4ECDC4;    /* Teal */
  --natalie-color: #9B59B6;  /* Purple */
}
```

### Emojis

Change the emoji for each sister in their HTML file:
- Look for `<span class="sister-emoji">` and update the emoji

## License

Private family website. All content belongs to the family.
