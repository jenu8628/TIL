<template>
  <div class="container mt-5 mb-5">
    <h1 align="center" style="margin-bottom: 50px">공지사항</h1>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  created() {
    console.log("!!!");
    this.$store.dispatch("delete_searchdata");
  }
};
</script>

<style></style>
