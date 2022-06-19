<template>
  <div class="container my-4">
    <div class="d-flex mx-5 justify-content-center" style="">
      <!-- <img src="@/assets/img/logo1.png" alt="" style="margin-right:15rem;"> -->
      <img src="@/assets/img/logo3.png" alt="">
    </div>
    <movie-carousel
    :topMovies="topMovies"
    ></movie-carousel>
    
  </div>
</template>

<script>
import MovieCarousel from '@/components/MovieCarousel.vue'
import { mapGetters } from 'vuex'

export default {
  name: "HomeView",
  data: function() {
    return {
      topMovies: []
    }
  },
  components: {
    MovieCarousel,
  },
  computed: {
    ...mapGetters(['movies'])
  }
  ,
  created() {
    console.log('Homeview Created!')
    setTimeout(() => {
      console.log(this.movies)
      this.topMovies = this.movies.slice().sort( function(a, b) {
            return b.popularity - a.popularity
          }).slice(0, 8)
      console.log(this.topMovies)
    }, 100)
  }

}
</script>

<style>
</style>