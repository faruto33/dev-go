<script setup>
// get provided config file
import { inject,ref } from 'vue'
import getApi from '../assets/api'
import axios from 'axios'

// get api url
const api = getApi('category','','',inject('config'))
// define the categories variable for column 1 and column2
let categories_cols = ref([[]])
let counter=ref(0)

// call url API to get the category list
axios.get(api).then(function (response) {
  let categories = response.data
  let i=1
  // split the data in 2 columns
  for(let item in categories)
  {
    if(categories_cols.value[i%2]===undefined)categories_cols.value[i%2]=[]
    categories_cols.value[i%2].push(item);
    i++;
 }
});
</script>

<template>
  <div class="row">
    <div v-for="n in 2" class="col-xs-5 col-sm-5 mx-auto">
      <div v-for="label,key in categories_cols[n-1]" class="mayday_home_collection-wrapper">
        <div class="mayday_home_collection-container_alt">
          <div href="/collections/Volontaires-HpAIC3ch" class="mayday_home_collection-container_col">
            <div @click="$emit('category',label)" class="mayday_home_collection">
              <div class="mayday_home_collection-inner">
                <div class="mayday_home_collection-img_wrapper" style="color: rgb(25, 95, 148);">
                  <svg aria-hidden="true" focusable="false" data-prefix="fal" data-icon="folder-open" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512" class="mayday_home_collection-img svg-inline--fa fa-folder-open fa-w-18"><path fill="currentColor" d="M527.95 224H480v-48c0-26.51-21.49-48-48-48H272l-64-64H48C21.49 64 0 85.49 0 112v288c0 26.51 21.49 48 48 48h385.057c28.068 0 54.135-14.733 68.599-38.84l67.453-112.464C588.24 264.812 565.285 224 527.95 224zM48 96h146.745l64 64H432c8.837 0 16 7.163 16 16v48H171.177c-28.068 0-54.135 14.733-68.599 38.84L32 380.47V112c0-8.837 7.163-16 16-16zm493.695 184.232l-67.479 112.464A47.997 47.997 0 0 1 433.057 416H44.823l82.017-136.696A48 48 0 0 1 168 256h359.975c12.437 0 20.119 13.568 13.72 24.232z" class=""></path>
                  </svg>
                </div>
                <div class="mayday_home_collection-title">
                {{ label }}
                </div>
                </div>di
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>


<style scoped>
.mayday_home_collection-wrapper {
    margin: 0 auto;
    max-width: 970px;
}
@media (min-width: 1000px) {
    .mayday_home_collection-container_alt {
        gap: 30px;
    }
}

.mayday_home_collection-container_alt {
    display: flex;
    flex-wrap: wrap;
    margin-top: 50px;
}

@media (max-width: 768px) {
.mayday_home_collection-container_alt {
    margin-top: 20px;
  }
}

@media (min-width: 768px) {
    .mayday_home_collection-container_col:not(:last-child) {
        border-right-width: 1px;
    }
}

.mayday_home_collection-container_col:not(:last-child) {
    --tw-border-opacity: 1;
    border-color: rgb(233 236 239 / var(--tw-border-opacity));
}

@media (min-width: 1000px) {
    .mayday_home_collection-container_col {
        width: 100%;
    }
}

@media (max-width: 768px) {
    .mayday_home_collection-container_col {
        width: 90%;
        margin:auto;
    }
}

.mayday_home_collection-container_col .mayday_home_collection {
    background: #fff;
    border: 2px solid #000;
    border-radius: 5px;
    color: #000;
    display: inline-block;
    font: 900 italic 16px / 48px Paris2024;
    height: 52px;
    overflow: hidden;
    padding: 0 50px 0 12px;
    position: relative;
    transition: background .2s linear, color .2s linear;
    width: 100%;
    z-index: 2;
}
@media (min-width: 768px) {
    .mayday_home_collection {
        border-radius: 0px;
    }
}

.mayday_home_collection {
    position: relative;
    cursor: pointer;
    border-radius: 4px;
}

.mayday_home_collection-container_col .mayday_home_collection-highlight, .mayday_home_collection-container_col .mayday_home_collection-img_wrapper {
    display: none;
}

@media (min-width: 768px) {
    .mayday_home_collection-highlight {
        opacity: 0;
    }
}

.mayday_home_collection-highlight {
    opacity: 1;
    transition-property: opacity;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 150ms;
}

@media (min-width: 768px) {
    .mayday_home_collection-highlight {
        height: 4rem;
        width: 16rem;
    }
}

.mayday_home_collection-highlight {
    position: absolute;
    z-index: 10;
    background-color: rgb(255 218 133 / var(--tw-bg-opacity));
    --tw-bg-opacity: 0.2;
    left: 0px;
    top: 0px;
    height: 5rem;
    width: 3rem;
}

.mayday_home_collection-container_col .mayday_home_collection-inner {
    flex-direction: row !important;
    height: 100%;
}

@media (min-width: 768px) {
    .mayday_home_collection-inner {
        flex-direction: column;
    }
}

.mayday_home_collection-inner {
    display: flex;
    flex-direction: row;
    align-items: center;
}

.mayday_home_collection-container_col .mayday_home_collection:after {
    background: #000;
    border-radius: 100px;
    content: url("data:image/svg+xml;charset=utf-8,%3Csvg width='12' height='10' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M12 5L8.853.5H6.524l2.413 3.484L0 3.9v2.198l8.916-.083L6.524 9.5h2.33L12 5z' fill='%23fff'/%3E%3C/svg%3E");
    height: 48px;
    position: absolute;
    padding: 0 45px 0 15px;
    right: -20px;
    top: 0;
    width: 48px;
}

.mayday_home_collection-container_col .mayday_home_collection-highlight, .mayday_home_collection-container_col .mayday_home_collection-img_wrapper {
    display: none;
}


.mayday_home_collection-img_wrapper {
    z-index: 30;
    display: flex;
    align-items: center;
    justify-content: center;
}

@media (min-width: 768px) {
    .mayday_home_collection-img_wrapper {
        margin-bottom: 1rem;
        height: 4rem;
        width: 4rem;
    }
}

.mayday_home_collection-img_wrapper {
    height: 3rem;
    width: 3rem;
    --tw-text-opacity: 1;
    color: rgb(0 0 0 / var(--tw-text-opacity));
}

.mayday_home_collection-container_col .mayday_home_collection-inner .mayday_home_collection-title {
    padding-right: 10px;
}

.mayday_home_collection-container_col .mayday_home_collection-inner .mayday_home_collection-title:hover {
    color:white;
}
.mayday_home_collection-container_col :hover{
  background:#000;
  transition: background .4s linear, color .4s linear;
  color:white;
}
@media (min-width: 768px) {
    .mayday_home_collection-title {
        overflow: hidden;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 3;
    }
}

.mayday_home_collection-title {
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}

@media (min-width: 768px) {
    .mayday_home_collection-title {
        text-align: center;
    }
}

.mayday_home_collection-title {
    text-align: left;
    font-size: 1.25rem;
    line-height: 1.75rem;
    font-weight: 700;
}

@media (min-width: 768px) {
    .mayday_home_collection-title {
        margin-left: 0px;
    }
}

.mayday_home_collection-title {
    margin-left: 1rem;
}

.mayday_home_collection-option {
    display: none;
}

</style>
