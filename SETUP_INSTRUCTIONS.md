# How to Run Jekyll Site Locally

Your site is a Jekyll-based GitHub Pages site that requires Jekyll to build and serve it locally. GitHub automatically runs Jekyll on their servers, which is why it works online but not locally without setup.

## One-Time Installation Steps

### 1. Install Ruby
- Download from: https://rubyinstaller.org/downloads/
- Choose **Ruby+Devkit 3.2.X or 3.4.X (x64)**
- During installation, check "Add Ruby executables to PATH"
- At the end, run `ridk install` when prompted (choose option 3)
- **Important:** After installation, restart VS Code completely (close all windows)

### 2. Install Bundler and Jekyll
Open PowerShell and run:
```powershell
gem install bundler jekyll
```

### 3. Fix Gemfile (if using Ruby 3.4+)
The `wdm` gem has compatibility issues with Ruby 3.4. Edit your `Gemfile` and comment out the wdm line:
```ruby
# gem "wdm", "~> 0.1.0" if Gem.win_platform?
```

### 4. Install Dependencies
Navigate to your project folder:
```powershell
cd "c:\Users\casto\Documents\GitHub\0-ccomploj.github.io"
bundle install
```

### 5. Run the Site Locally
```powershell
bundle exec jekyll serve --host 127.0.0.1
```

Your site will be available at: http://127.0.0.1:4000

## Quick Start (After Initial Setup)

Every time you want to run the site:
```powershell
cd "c:\Users\casto\Documents\GitHub\0-ccomploj.github.io"
bundle exec jekyll serve --host 127.0.0.1
```

Then open your browser to: http://127.0.0.1:4000

To stop the server: Press `Ctrl+C` in the terminal

## How It Works

- **Jekyll** converts your `.md` files and `_config.yml` into HTML/CSS/JS
- **Bundler** manages all the Ruby gem dependencies (like the minimal-mistakes theme)
- The `--host 127.0.0.1` flag ensures the server binds to localhost properly on Windows
- Auto-regeneration is enabled by default - changes to files (except `_config.yml`) will automatically rebuild the site

## Troubleshooting

### If `gem` command is not recognized:
- Restart VS Code completely (close all windows)
- Or manually add `C:\Ruby34-x64\bin` to your Windows PATH environment variable

### If you get SSL errors:
```powershell
gem install rubygems-update
update_rubygems
```

### If bundle install fails:
```powershell
gem update --system
bundle update
```

### If you get "connection refused" errors:
Make sure you're using `--host 127.0.0.1` when starting the server and accessing http://127.0.0.1:4000 (not localhost:4000)

### Missing favicon errors:
These are harmless warnings about missing icon files. Your site will work fine without them.
