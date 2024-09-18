<script setup>
import { ref } from 'vue'

</script>

<template>
<div class="mayday_header-container" home-view="true">
  <div class="mayday_header-main mayday_header-main_fixed">
    <div class="mayday_header-nav">
      <div class="mayday_header-company_logo_wrapper nuxt-link-active">
      <img alt="logo entreprise" src="https://sftpstgchqi54noyumqk.blob.core.windows.net/paris-2024/static/___lj1t7tdoamd5jzpj.blob" class="mayday_header-company_logo cursor-pointer">
      </div>
    </div>
  </div>
  <div id="header-search" class="mayday_header-home_view mayday_header-home_view_visible">
    <div class="flex w-full justify-center">
      <div class="mayday_search-wrapper_main">
        <div class="transition-all duration-500">
          <div class="z-[60] h-16 text-bold duration-300 transition-opacity text-center opacity-100">
            <div class="mayday_search-wrapper_label_text">
              <span data-v-70cf18ea=""> Comment peut-on vous</span>
              <span class="mayday_search-wrapper_label_text_highlight">aider ?</span>
            </div>
          </div>
        </div>
        <div class="z-[80] transition-transform duration-500 mx-4 md:mx-0 mayday_search-bar opacity-100">
          <div class="w-full relative pointer-events-auto">
            <div class="mayday_search-input_group">
              <div class="mayday_search-input_wrapper mayday_search-input_wrapper_focus mayday_search-input_wrapper_home">
                <svg aria-hidden="true" focusable="false" data-prefix="fal" data-icon="search" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="mayday_search-input_icon svg-inline--fa fa-search fa-w-16">
                  <path fill="currentColor" d="M508.5 481.6l-129-129c-2.3-2.3-5.3-3.5-8.5-3.5h-10.3C395 312 416 262.5 416 208 416 93.1 322.9 0 208 0S0 93.1 0 208s93.1 208 208 208c54.5 0 104-21 141.1-55.2V371c0 3.2 1.3 6.2 3.5 8.5l129 129c4.7 4.7 12.3 4.7 17 0l9.9-9.9c4.7-4.7 4.7-12.3 0-17zM208 384c-97.3 0-176-78.7-176-176S110.7 32 208 32s176 78.7 176 176-78.7 176-176 176z" class=""></path>
                </svg>
                <div class="max-width-62 relative">
                  <div class="flex tags-wrapper"></div>
                </div>
                <input v-model="search" v-on:keyup.enter="$emit('search',search)" placeholder="Rechercher dans le centre d’aide" maxlength="500" spellcheck="false" size="1" class="mayday_search-input">
                <button type="button" @click="$emit('search',search)" class="btn btn-outline-primary">Rechercher</button>
              </div>
            </div>
            <div data-v-ae6a6fd8="" class="mayday_loaders-line_container h-2"></div>
            <div class="pb-4 search-results dropdown" style="display: none;">
              <div class="overflow"></div>
            </div>
          </div>
        </div>
      </div>
      </div><div></div>
    </div>
  </div>
  <div data-v-ae6a6fd8="" class="mayday_loaders-line_container mayday_header-loading">
  </div>
</template>


<style scoped>

@media (min-width: 768px) {
    .md\:mx-0 {
        margin-left: 0px;
        margin-right: 0px;
    }
}
@media (min-width: 768px) {
    .mayday_search-bar {
        padding-left: 25%;
        padding-right: 25%;
    }
}
.mayday_search-bar {
    pointer-events: none;
}

@media (min-width: 768px) {
    .md\:mx-0 {
        margin-left: 0px;
        margin-right: 0px;
    }
}
.mayday_search-input_group {
    display: flex;
    height: 3rem;
    flex-direction: row;
    gap: 0.5rem;
}

.duration-500 {
    transition-duration: 500ms;
}
.transition-transform {
    transition-property: transform;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 150ms;
}
.opacity-100 {
    opacity: 1;
}
.mx-4 {
    margin-left: 1rem;
    margin-right: 1rem;
}

.mayday_search-input {
    width: 100%;
    text-overflow: ellipsis;
    font-size: 1.125rem;
    line-height: 1.5rem;
    border-style: none;
    background-color: transparent;
    outline: 2px solid transparent;
    outline-offset: 2px;
}

.mayday_search-input_group {
    display: flex;
    height: 3rem;
    flex-direction: row;
    gap: 0.5rem;
}

mayday_search-input {
    width: 100%;
    text-overflow: ellipsis;
    font-size: 1.125rem;
    line-height: 1.5rem;
    border-style: none;
    background-color: transparent;
    outline: 2px solid transparent;
    outline-offset: 2px;
}

@media (min-width: 1000px) {
    .mayday_header-container .mayday_search-input_wrapper {
        margin: 0;
    }
}

.mayday_header-container .mayday_search-input_wrapper {
    background: #fff;
    box-shadow: 0 1px 11px rgba(0, 0, 0, .15);
    color: #000;
    margin-bottom: -30px;
}

.mayday_search-input_wrapper_home {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
    padding-right: 1rem !important;
}

.mayday_search-input_wrapper_focus {
    --tw-bg-opacity: 1;
    background-color: rgb(252 252 255 / var(--tw-bg-opacity));
    --tw-text-opacity: 1;
    color: rgb(0 0 0 / var(--tw-text-opacity));
}

.mayday_search-input_wrapper {
    display: flex;
    align-items: center;
    background-color: rgb(252 252 255 / 0.2);
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 300ms;
    border-radius: 4px;
    width: 100%;
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
    padding-right: 1.25rem;
    padding-left: 0.5rem;
}

.svg-inline--fa, svg:not(:root).svg-inline--fa {
    overflow: visible;
}

.svg-inline--fa.fa-w-16 {
    width: 1em;
}

.mayday_search-input_icon {
    padding-right: 0.5rem;
    font-size: 1rem;
    line-height: 1.5rem;
    width: 32px !important;
}

.svg-inline--fa {
    display: inline-block;
    font-size: inherit;
    height: 1em;
    vertical-align: -.125em;
}

img, svg, video, canvas, audio, iframe, embed, object {
    display: block;
    vertical-align: middle;
}

.text-primary {
    --tw-text-opacity: 1;
    color: rgb(0 0 0 / var(--tw-text-opacity));
}

.mayday_header-container {
    background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg width='1440' height='360' fill='none' preserveAspectRatio='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cg clip-path='url(%23a)'%3E%3Cg clip-path='url(%23b)'%3E%3Cpath fill='url(%23c)' d='M0 0h1440v351H0z'/%3E%3Cpath d='M360 128H0v340h360V128z' fill='url(%23d)'/%3E%3Cpath d='M1440 128h-360v351h360V128z' fill='url(%23e)'/%3E%3Cpath d='M1080 200H360v351h720V200z' fill='url(%23f)'/%3E%3C/g%3E%3Cg clip-path='url(%23g)'%3E%3Cpath fill='url(%23h)' d='M0 0h1440v360H0z'/%3E%3Cpath transform='rotate(-180 720 270)' fill='url(%23i)' d='M720 270h2160v90H720z'/%3E%3Cpath transform='rotate(-180 2880 360)' fill='url(%23j)' d='M2880 360h2160v90H2880z'/%3E%3C/g%3E%3C/g%3E%3Cdefs%3E%3ClinearGradient id='c' x1='671' y1='-81.5' x2='671' y2='476' gradientUnits='userSpaceOnUse'%3E%3Cstop stop-color='%23331362'/%3E%3Cstop offset='1' stop-color='%237D84C2'/%3E%3C/linearGradient%3E%3ClinearGradient id='d' x1='167.75' y1='49.054' x2='167.75' y2='589.083' gradientUnits='userSpaceOnUse'%3E%3Cstop stop-color='%23331362'/%3E%3Cstop offset='1' stop-color='%237D84C2'/%3E%3C/linearGradient%3E%3ClinearGradient id='e' x1='1247.75' y1='46.5' x2='1247.75' y2='604' gradientUnits='userSpaceOnUse'%3E%3Cstop stop-color='%23331362'/%3E%3Cstop offset='1' stop-color='%237D84C2'/%3E%3C/linearGradient%3E%3ClinearGradient id='f' x1='695.5' y1='118.5' x2='695.5' y2='676' gradientUnits='userSpaceOnUse'%3E%3Cstop stop-color='%23331362'/%3E%3Cstop offset='1' stop-color='%237D84C2'/%3E%3C/linearGradient%3E%3ClinearGradient id='h' x1='-47.857' y1='178.774' x2='1512.86' y2='178.774' gradientUnits='userSpaceOnUse'%3E%3Cstop stop-color='%23009CE0'/%3E%3Cstop offset='1' stop-color='%23022366'/%3E%3C/linearGradient%3E%3ClinearGradient id='i' x1='662.5' y1='314.694' x2='2989.29' y2='314.697' gradientUnits='userSpaceOnUse'%3E%3Cstop stop-color='%23022366'/%3E%3Cstop offset='.674' stop-color='%23009CE0'/%3E%3Cstop offset='1' stop-color='%23FBA9CB'/%3E%3C/linearGradient%3E%3ClinearGradient id='j' x1='2822.5' y1='404.694' x2='5149.29' y2='404.697' gradientUnits='userSpaceOnUse'%3E%3Cstop stop-color='%23022366'/%3E%3Cstop offset='.674' stop-color='%23009CE0'/%3E%3Cstop offset='1' stop-color='%23FBA9CB'/%3E%3C/linearGradient%3E%3CclipPath id='a'%3E%3Cpath fill='%23fff' d='M0 0h1440v360H0z'/%3E%3C/clipPath%3E%3CclipPath id='b'%3E%3Cpath fill='%23fff' d='M0 0h1440v360H0z'/%3E%3C/clipPath%3E%3CclipPath id='g'%3E%3Cpath fill='%23fff' d='M0 0h1440v360H0z'/%3E%3C/clipPath%3E%3C/defs%3E%3C/svg%3E");
    background-size: 100% 100%;
    position: relative;
    z-index: 50;
}

.mayday_header-container {
    width: 100%;
    height: 240px;
    box-shadow: 0 5px 14px rgba(0, 0, 0, .15);
}

@media (min-width: 1000px) {
    .mayday_header-container .mayday_search-input_wrapper {
        margin: 0;
    }
}

.mayday_search-input_wrapper_home {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}
.mayday_search-input_wrapper_focus {
    --tw-bg-opacity: 1;
    background-color: rgb(252 252 255 / var(--tw-bg-opacity));
    --tw-text-opacity: 1;
    color: rgb(0 0 0 / var(--tw-text-opacity));
}
.mayday_search-input_wrapper {
    display: flex;
    align-items: center;
    background-color: rgb(252 252 255 / 0.2);
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 300ms;
    border-radius: 4px;
    width: 100%;
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
    padding-right: 1.25rem;
    padding-left: 0.5rem;
}

.mayday_layout-container {
    background: #f9f9f9;
    font-family: "Source Sans 3", "ui-sans-serif", "system-ui", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "Roboto", "Helvetica Neue", "Arial", "Noto Sans", "sans-serif", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !important;
}

.mayday_layout-container {
    background-color: rgb(252 252 255 / var(--tw-bg-opacity));
    font-family: Lato, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}

mayday_header-container .mayday_header-main {
    background: none;
    height: 140px;
    padding-top: 20px;
}

.mayday_header-main_fixed {
    position: relative !important;
}

@media (min-width: 1024px) {
    .mayday_header-main {
        padding-left: 5rem;
        padding-right: 5rem;
    }
}

@media (min-width: 768px) {
    .mayday_header-main {
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }
}

.mayday_header-main {
    background-color: rgb(1 1 1 / var(--tw-bg-opacity));
    position: fixed;
    z-index: 45;
    height: 4rem;
    width: 100%;
    padding-left: 1rem;
    padding-right: 1rem;
}

@media (min-width: 1000px) {
    .mayday_header-container .mayday_header-company_logo {
        height: 140px;
    }
}

.mayday_header-container .mayday_header-company_logo {
    height: 90px;
    max-height: none;
}
.mayday_header-company_logo {
    max-height: 3rem;
    max-width: 20rem;
    z-index: 100;
    -o-object-fit: contain;
    object-fit: contain;
}
.cursor-pointer {
    cursor: pointer;
}

.mayday_header-container .mayday_header-company_logo_wrapper {
    max-height: none;
    margin-left: 58%;
    transform: translateX(-50%);
}

.mayday_header-company_logo_wrapper {
    display: flex;
    max-height: 3rem;
    max-width: 20rem;
    top: 1rem;
    z-index: 100;
}

@media (min-width: 1000px) {
    .mayday_header-container .mayday_search-wrapper_label_text {
        font: 900 48px / 52px Paris2024;
    }
}

.mayday_header-container .mayday_search-wrapper_label_text {
    display: inline-block;
    font: 900 36px / 40px Paris2024;
    text-transform: uppercase;
}

@media (min-width: 768px) {
    .mayday_search-wrapper_label_text {
        font-size: min(2.5vw, 40px);
    }
}

.mayday_search-wrapper_label_text {
    display: flex;
    height: 100%;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    text-overflow: ellipsis;
    font-size: min(6vw, 40px);
}

.mayday_header-home_view{
  color:#f9f9f9;
  margin-top: 50px;
}

.mayday_loaders-line_container[data-v-ae6a6fd8] {
    z-index: 40;
    display: flex;
    height: 0.25rem;
    width: 100%;
    align-items: center;
    justify-content: center;
}

.mayday_header-loading {
    position: fixed;
    top: 4rem;
    width: 100%;
}
.max-width-62 {
    max-width: 62%;
}
.relative {
    position: relative;
}
.w-full {
    width: 100%;
}
.relative {
    position: relative;
}

.pointer-events-auto {
    pointer-events: auto;
}

a {
    color: inherit;
    text-decoration: inherit;
}

html {
    line-height: 1.5;
    -webkit-text-size-adjust: 100%;
    -moz-tab-size: 4;
    -o-tab-size: 4;
    tab-size: 4;
    font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    font-feature-settings: normal;
    font-variation-settings: normal;
    background: #f4f4f4;
}

</style>
