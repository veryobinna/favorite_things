<template>
<div>
     <div v-bind:key="category.id" v-for="category in categories" >
           {{ category.name}}
     </div>
</div>
</template>

<script>
export default {
     name: "Categories",
     props:["categories"]
}
</script>


<style scoped>

</style>
