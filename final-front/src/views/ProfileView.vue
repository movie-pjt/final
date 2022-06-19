<template>
  <div class="container my-5">
      <div class=" mx-5" style="flex-grow:1">
        <div class="mx-2 my-2 d-flex py-3 justify-content-between">
          <div class="border-div col-3 profile-username">
            <h1>{{ profile.username }}</h1>
          </div>
          <div class="border-div col-8 d-flex px-3 py-3">
            <div class="d-flex flex-column mx-3">
              <div class="static-title">관심 영화</div>
              <div>{{ profile.like_movies.length }}</div>
            </div>
            <div class="d-flex flex-column">
              <div class="static-title">리뷰</div>
              <div>{{ profile.reviews.length }}</div>
            </div>
            <div class="d-flex flex-column mx-3">
              <div class="static-title">게시글</div>
              <div>{{ profile.articles.length }}</div>
            </div>
          </div>
        </div>
        <div class="border-div mx-2 my-2 mb-3">
          <h1>LikeMovie</h1>
          <div>
            <div class="mx-3">
              <div class="container d-flex d-flex flex-nowrap flex-row" style="overflow-y:hidden;">
                <movie-card
                  v-for="(movie, idx) in profile.like_movies"
                  :key="idx"
                  :movie="movie"
                  class=""
                  ></movie-card>
                </div>
            </div>
          </div>
        </div>
        <div class="border-div mx-2 my-2 mb-3">
          <h1>recommendMovies</h1>
          <div class="mx-3">
            <div style="">
              <div class="container d-flex d-flex flex-nowrap flex-row" style="overflow-y:hidden;">
                <movie-card
                  v-for="(movie, idx) in recommendMovies"
                  :key="idx"
                  :movie="movie"
                  class=""
                  ></movie-card>
                </div>
            </div>
          </div>
        </div>
        <div class="border-div mx-2 my-2 mb-3">
          <h1>Articles</h1>
          <profile-article-list
          v-for="article in profile.articles"
          :key="article.pk"
          :article="article"
          >

          </profile-article-list>
        </div>
        <div class="border-div mx-2 my-2">
          <h1>Reviews</h1>
          <review-list-item
          v-for="(review, idx) in profile.reviews"
          :key="idx"
          :review="review"
          ></review-list-item>
        </div>
        
      </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import MovieCard from '@/components/MovieCard.vue'
import ReviewListItem from '@/components/ReviewListItem.vue'
import ProfileArticleList from '@/components/ProfileArticleList.vue'

export default {
  name: 'ProfileView',
  components: {
    MovieCard,
    ReviewListItem,
    ProfileArticleList,
  },
  computed: {
    ...mapGetters(['profile', 'currentUser', 'recommendMovies'])
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchRecommendMovies']),
    imgSrc: (imgPath) => {
      return "https://image.tmdb.org/t/p/original" + imgPath
    },
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    this.fetchRecommendMovies()
  }
}
</script>

<style>
  .profile-div {
    border: 1px solid white;
    /* border-radius: 2rem; */
    
    padding-top: 2rem;
    padding-bottom: 2rem;
  }
  .border-div {
    background-color: #202020;
    border-radius: 10px;
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
  }
  .static-title {
    font-size: 1.2rem;
    font-family: 'Hahmlet';
    font-weight: 700;
  }
</style>