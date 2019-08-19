<template>
<div>
     <div v-bind:key="favoriteThing.id" v-for="favoriteThing in favoriteThings" >
           {{ favoriteThing.title}}
     </div>
</div>
</template>

<script>
export default {
     name: "FavoriteThings",
     props:["favoriteThings"]

}
</script>


<style scoped>

</style>
