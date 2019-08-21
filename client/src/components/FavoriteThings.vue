<template>
<div>
          <p class="subtitle">My Favorite things in {{favoriteThingsObj.name}}</p>
     <div v-bind:key="favoriteThing.id" v-for="favoriteThing in favoriteThingsObj.favorite_things" >
          <FavoriteThingItem 
          v-on:updateFavoriteThing="(newItem)=>$emit('updateFavoriteThing',newItem)"
          v-bind:favoriteThing="favoriteThing"
          v-bind:categories="categories"/>
     </div>
</div>
</template>

<script>
import FavoriteThingItem from './FavoriteThingItem.vue';

export default {
     name: "FavoriteThings",
     props:["favoriteThingsObj", "categories"],
     components:{
          FavoriteThingItem
     }

}
</script>


<style scoped>

</style>
