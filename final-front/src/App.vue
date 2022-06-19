<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view/>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    NavBar,
  },
  computed: {
    ...mapGetters(['movies'])
  },
  methods: {
    ...mapActions(['fetchMovies', 'fetchCurrentUser']),
  },
  created () {
    this.fetchMovies();
    this.fetchCurrentUser();
  }
}
</script>


<style>

#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: 'Pretendard';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /* color: #2c3e50; */
  color: #ffffff;
}

#app h1 {
  font-family: 'Hahmlet';
  font-weight: 800;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #ffffff;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
