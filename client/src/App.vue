<template>
  <div id="app">
    <div >
        <Categories v-bind:categories="categories"/>
        <FavoriteThings  v-bind:favoriteThings="favoriteThings"/>
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import FavoriteThings from './components/FavoriteThings.vue';
import Categories from './components/Categories.vue';
import Category from './components/Category.vue';
import axios from 'axios';

export default {
  name: 'app',
  components: {
    FavoriteThings,
    Categories
  },
  data(){
    return {
      favoriteThings: [],
      categories: []
    }
  },
  created(){
    axios.get(
      'http://127.0.0.1:8000/category/',
    ).then(
      res => this.categories = res.data.results
      ).catch(err => console.log(err))

    axios.get(
      'http://127.0.0.1:8000/favorite_things/',
    ).then(
      res => this.favoriteThings = res.data.results
      ).catch(err => console.log(err))
  }
}
</script>
<style>
#app {

}
</style>
