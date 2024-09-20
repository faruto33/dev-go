<script setup>
import Header from './components/Header.vue'
import Tree from './components/Tree.vue'
import Search from './components/Search.vue'
import Home from './components/Home.vue'
import Breadcrumb from './components/Breadcrumb.vue'
import { ref } from 'vue'

// display home page by default
let home= ref(true)
let query = ref()
let category = ref()

// search by keyword
function searchkeyword(event){
  // new keyword
  query.value = event
  // empty the category search
  category.value = ''
  // stop displaying the home page
  home.value = false
}

// search by category
function searchcategory(event){
  // new category
  category.value = event
  // empty the query search
  query.value=''
  // stop displaying the home page
  home.value = false
}

// function to return to home page
function returnhome(event){
  home.value = true
}

</script>

<template>
  <div class="row">
    <div class="col">
      <Header v-on:search="searchkeyword($event)"/>
    </div>
  </div>
  <div v-show="!home" class="row  bg-light">
    <div class="col-xs-12 col-sm-12 mx-auto">
      <Breadcrumb v-on:returnhome="returnhome($event)"/>
    </div>
  </div>
  <div class="row bg-light">
    <div v-show="home" class="col-xs-12 col-sm-12 mx-auto">
      <main>
        <Home v-on:category="searchcategory($event)"/>
      </main>
    </div>
    <div v-show="!home" class="col-xs-3 col-sm-3 mx-auto tree-container">
      <main>
        <Tree v-on:category="searchcategory($event)"/>
      </main>
    </div>
    <div v-show="!home" class="col-xs-7 col-sm-7">
      <main>
        <Search :query="query" :category="category"/>
      </main>
    </div>
    <div class="col-xs-1 col-sm-1"></div>
  </div>

</template>
