<template>
  <div class="px-3 my-3 mx-3 movie-card-div" style="width: 225px;"
  @click="movieCardClick"
  >
    <div class="movie-card" style="width: 225px;">
      <img
      style="width: 225px; height: 341px;"
      :src="imgSrc(movie.poster_path)" class="card-img-top" alt="...">
      <div class="movie-card-body d-flex flex-column justify-content-center align-items-start px-4">
        <div class="movie-card-title">{{ movie.title }}</div>
        <div class="movie-card-release-date">{{ movie.release_date }}</div>
      </div>
    </div>
    
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  name: 'MovieCard',
  props: {
    movie: Object
  },
  methods: {
    ...mapActions(['fetchMovie']),
    imgSrc: (imgPath) => {
      return "https://image.tmdb.org/t/p/original" + imgPath
    },
    movieCardClick: function () {
      // this.fetchMovie(this.movie.id)
      this.$router.push({name: 'movie_detail', params:{moviePk: this.movie.id}})
      // this.$emit('movie-card-click', this.movie.id)
    }
  }
}
</script>

<style>
  .movie-card {
    cursor:pointer;
    box-shadow: rgba(255, 255, 255, 0.24) 0px 3px 8px;
    transition: 0.3s;
  }
  .movie-card:hover {
    box-shadow: rgba(255, 255, 255, 0.24) 0px 9px 19px, rgba(255, 255, 255, 0.24) 0px 7px 6px;
    transform: translateY(-6px);
  }
  

  .movie-card {
    color: white;
    background-color: #202020;
    border-radius: 8px;
  }
  .movie-card-body {
    height: 6rem;
  }
  .movie-card-title {
    font-size: 1.3rem;
    font-family: 'Hahmlet';
    font-weight: 800;
  }
</style>