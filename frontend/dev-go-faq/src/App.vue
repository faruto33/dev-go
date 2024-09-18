<script setup>
import Header from './components/Header.vue'
import TheWelcome from './components/TheWelcome.vue'
import Search from './components/Search.vue'
import { ref } from 'vue'

let query = ref('Recrutement')

function searchsend(event){
  query.value = event
}

</script>

<template>
  <div class="row">
    <div class="col">
      <Header v-on:search="searchsend($event)"/>
    </div>
  </div>
  <div class="row bg-light">
    <div class="col-xs-10 col-sm-3">
      <main>
        <TheWelcome />
      </main>
    </div>
    <div class="col-xs-10 col-sm-7">
      <main>
        <Search :query="query"/>
      </main>
    </div>
  </div>

</template>
