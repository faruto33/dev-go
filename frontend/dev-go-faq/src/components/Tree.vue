<template>
  <h4>CATEGORIES</h4>
  <treeview :config="config" :nodes="nodes"
    @nodeFocus="focus('node-focus',$event)"
    </treeview>
</template>

<script setup>
import { nodesEncode,nodesConfig } from "../assets/node"
import { ref,defineEmits,inject } from 'vue'
import getApi from '../assets/api'
import axios from 'axios'
import treeview from "vue3-treeview";
import "vue3-treeview/dist/style.css";

// get api url
const api = getApi('category','','',inject('config'))

// define nodes and and tree config
let nodes=ref('')
let config=ref('')
// define variable to emit category event
const emit = defineEmits(['category'])
// en focuse trigger category event
function focus(e,x){
  emit('category', x.text)
}

// search for the tree node elements in API
// encode results to be compatible
// create the tree config
function search() {
      axios
      .get(api)
      .then(function (response) {
        nodes.value = nodesEncode(response.data)
        config.value = nodesConfig(response.data)
      });
    }

// call the search function to display the tree
search()
</script>

<style>

.checkbox-wrapper {
  background: #fff !important;
  border: 0 !important;
}
.node-wrapper{
      cursor: pointer;
}
.icon-wrapper{
  width: 7px !important;
}

</style>
