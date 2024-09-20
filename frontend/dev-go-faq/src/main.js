import './assets/main.css'
import './assets/bootstrap.min.css'
import 'bootstrap'

import { createApp } from 'vue'
import App from './App.vue'
import { config } from './assets/config'

// create a new app
const app = createApp(App);

// define global config properties
app.config.globalProperties.msg = 'hello'
app.provide('config', config)

// mount the application
app.mount('#app');
