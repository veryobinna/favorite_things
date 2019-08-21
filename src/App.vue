<template>
  <div id="app">
    <div id="nav">
      <Header/>
    </div>
    <router-view/>
  </div>
</template>
<script>
import Header from './components/layout/Header.vue';
export default {
  name: 'App',
  components: {
    Header,
  },
}
</script>

<style>
#app {

}
</style>
