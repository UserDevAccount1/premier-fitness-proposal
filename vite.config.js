import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// BASE_PATH=/ for container/root deploys; defaults to GitHub Pages subpath
export default defineConfig({
  plugins: [vue()],
  base: process.env.BASE_PATH || '/premier-fitness-proposal/',
})
