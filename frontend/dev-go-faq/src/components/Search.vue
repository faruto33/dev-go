<script setup>
import Loader from './Loader.vue'
import axios from 'axios'
import { ref, watchEffect,inject } from 'vue'
import getApi from '../assets/api'

// define the query and category string get from parent component
const props = defineProps({query: String,category: String})
// get the provided api config
const apiconfig = ref(inject('config'))

// define reactive variable to display results
let labels = ref('')
let bodys = ref('')
let api = ref('')
// define reactive variable to display loader
const loading = ref(false)
// define reactive variable to set body visible
let isVisible = ref([])

function search() {
    //display the loader
    loading.value = true
    // get api url
    axios
    .get(getApi('search',props.query,props.category,apiconfig.value))
    .then(function (response) {
      // update results
      labels.value = response.data.label;
       // update results
      bodys.value = response.data.body;
      // remove the loader after loading
      loading.value= false
    });
    }

// update element visibility
function toggleVisibility(key){
  isVisible.value[key]= !(isVisible.value[key])
}
// if props change we start a new start
watchEffect(() => {
  search()
})
</script>


<template>
  <results>
    <Loader v-if="loading"></Loader>
    <div v-else class="mayday_layout-loading_content">
      <div class="mayday_folder-container">
        <h1 class="mayday_folder-title">
        </h1>
        <section class="mayday_folder-entities_container">
          <ul class="mayday_folder-entities_list">
            <li v-for="label,key in labels" class="mayday_folder-entities_item">
              <div class="mayday_entity-link" @click="toggleVisibility(key)">
                <div class="mayday_entity-wrapper">
                  <div class="mayday_entity-title">
                    <div class="mayday_entity-icon">
                      <div class="mayday_base-icon" style="font-size: 20px; width: 20px; height: 20px;">
                        <svg aria-hidden="true" focusable="false" data-prefix="fal" data-icon="file-alt" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" color="" class="svg-inline--fa fa-file-alt fa-w-12">
                          <path fill="currentColor" d="M369.9 97.9L286 14C277 5 264.8-.1 252.1-.1H48C21.5 0 0 21.5 0 48v416c0 26.5 21.5 48 48 48h288c26.5 0 48-21.5 48-48V131.9c0-12.7-5.1-25-14.1-34zm-22.6 22.7c2.1 2.1 3.5 4.6 4.2 7.4H256V32.5c2.8.7 5.3 2.1 7.4 4.2l83.9 83.9zM336 480H48c-8.8 0-16-7.2-16-16V48c0-8.8 7.2-16 16-16h176v104c0 13.3 10.7 24 24 24h104v304c0 8.8-7.2 16-16 16zm-48-244v8c0 6.6-5.4 12-12 12H108c-6.6 0-12-5.4-12-12v-8c0-6.6 5.4-12 12-12h168c6.6 0 12 5.4 12 12zm0 64v8c0 6.6-5.4 12-12 12H108c-6.6 0-12-5.4-12-12v-8c0-6.6 5.4-12 12-12h168c6.6 0 12 5.4 12 12zm0 64v8c0 6.6-5.4 12-12 12H108c-6.6 0-12-5.4-12-12v-8c0-6.6 5.4-12 12-12h168c6.6 0 12 5.4 12 12z" class=""></path>
                        </svg>
                      </div>
                    </div>
                      <div class="mayday_entity-label">{{ label }}</div>
                  </div>
                </div>
              </div>
              <div v-if=isVisible[key] class="mayday_entity-body">{{ bodys[key] }}</div>
            </li>
          </ul>
        </section>
      </div>
    </div>
  </results>
</template>

<style lang="css" scoped>
.mayday_layout-loading_content {
    height: 100%;
    width: 100%;
}
.mayday_folder-container {
    position: relative;
    margin-top: 0px;
    padding-left: 0px;
    padding-right: 0px;
}
@media (min-width: 768px) {
    .mayday_folder-title {
        margin-left: 0.5rem;
    }
}
.mayday_folder-title {
    margin-top: -0.25rem;
    display: flex;
    align-items: center;
    font-size: 1.875rem;
    line-height: 2.25rem;
    font-weight: 700;
}
@media (min-width: 768px) {
    .mayday_folder-entities_container{
        padding-left: 0.5rem;
    }
}
.mayday_folder-entities_list{
    margin-top: 0.75rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
}

.mayday_knowledge-wrapper .mayday_folder-dropdown_list, .mayday_knowledge-wrapper .mayday_folder-entities_list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.mayday_entity-wrapper {
    cursor: pointer;
    border-radius: 4px;
    --tw-bg-opacity: 1;
    background-color: rgb(255 255 255 / var(--tw-bg-opacity));
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
    padding-left: 0.75rem;
    padding-right: 0.75rem;
}
.mayday_knowledge-wrapper .mayday_entity-wrapper {
    background: none !important;
    padding: 0 !important;
}
.mayday_entity-title{
    display: flex;
}
.mayday_knowledge-wrapper .mayday_entity-wrapper .mayday_entity-icon {
  background: none !important;
}
.mayday_entity-icon {
  margin-top: 0.25rem;
  display: flex;
  height: 1.25rem;
  width: 1.25rem;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity));
}
.mayday_entity-label {
    margin-left: 0.5rem;
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    font-size: 1.25rem;
    line-height: 2.7rem;
    font-weight: 700;
}

.mayday_entity-wrapper .mayday_entity-label {
    font-size: 16px !important;
    font-weight: 500 !important;
}

.mayday_entity-wrapper:hover {
    --tw-text-opacity: 1;
    color: rgb(0 0 0 / var(--tw-text-opacity));
}
.mayday_entity-link:after {
    content: url("data:image/svg+xml;charset=utf-8,%3Csvg width='22' height='22' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M19.277 10.667l-4.423-6h-2.197l3.69 5.042L3.39 9.625v2.056l12.957-.084-3.69 5.07h2.197l4.423-6z' fill='%23000'/%3E%3C/svg%3E");
    right: 10px;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
}

.mayday_entity-link, .mayday_folder-entity_container .mayday_folder-entity_wrapper {
    border-radius: 5px;
    font-size: 14px;
    padding: 0 30px 0 0;
    position: relative;
    background: white;
    cursor: pointer;
}

.mayday_entity-link {
    display: block;
    border-radius: 4px;
    border-width: 1px;
    border-color: transparent;
    --tw-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
    --tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 200ms;
    transition-timing-function: linear;
}

ol, ul, menu {
    list-style: none;
    margin: 0;
    padding: 0;
}

.mayday_entity-body {
    border-radius: 4px;
    border-width: 10px;
    border-color: transparent;
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
    transition-property: all;
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    transition-duration: 200ms;
    transition-timing-function: linear;
    background-color: #edc2de2b;
    margin-top: 5px;
    padding: 20px;
}
</style>
