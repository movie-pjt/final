<template>
  <div class="my-5">
    <div class="container">
      <h1 class="view-title text-start">영화 목록</h1>
      <div
      class="sort-list row d-flex justify-content-center">
          <div class="d-flex justify-content-end align-items-center">
            <!-- <a href="" class="sort-link">관객수</a>
            <a href="" class="sort-link">평점</a>
            <a href="" class="sort-link">좋아요</a> -->
            <a
            v-for="(sortKey, idx) in Object.keys(orderedListOptions)"
            :key="idx"
            @click="sortOrder = sortKey"
            :class="{ sortActive: (sortOrder === sortKey) }"
            class="sort-link"
            >{{sortKey}}</a>
          </div>
        <div class="d-flex justify-content-between align-items-end">
        </div>
        <b-modal v-model="modalShow" hide-footer hide-header size="xl" @hidden="closeModal">
          <img :src="imgSrc(movie.backdrop_path)" alt="" class="modal-img">
          <div class="mx-5 my-5">
            <div class="container">
              <div class="d-flex">
                <iframe
                class="col-lg-6 col-12"
                width="600" height="400" :src="videoSrc(movie.video_path)" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                <div class="d-flex flex-column mx-5" style="width:100%">
                  <div class="d-flex align-items-center">
                    <img v-if="!movie.adult" src="@/assets/img/age_15.png" alt="" style="width:40px; height:40px; margin-right: 0.5rem; margin-top: 8px;">
                    <img v-if="movie.adult" src="@/assets/img/age_18.png" alt="" style="width:40px; height:40px; margin-right: 0.5rem; margin-top: 8px;">
                    <div class="d-flex align-items-center movie-detail-title">{{ movie.title }}</div>
                  </div>
                  <div class="d-flex justify-content-between mb-2 movie-detail-info">
                    <div class="movie-detail-vote-average d-flex align-items-center">
                        <img src="@/assets/img/star.png" alt=""
                        style="width: 20px;"
                        >
                        <span class="mx-1">{{ movie.vote_average }}</span>
                    </div>
                    <div class="d-flex">
                      <div class="mx-1">{{ movie.release_date }}</div>
                      <div class="mx-1">{{ getPlayTime(movie.play_time) }}</div>
                    </div>
                  </div>
                  <div class="d-flex justify-content-between my-2">
                    <div>
                      <a :href="netflixSrc(movie.netflix_path)" target="_blank" v-if="movie.netflix_path">
                        <img 
                        class="movie-ott-img mx-1"
                        src="@/assets/img/button_netflix.png" alt="">
                      </a>
                      <a :href="watchaSrc(movie.watcha_path)" target="_blank" v-if="movie.watcha_path">
                        <img 
                        class="movie-ott-img mx-1"
                        src="@/assets/img/button_watcha.png" alt="">
                      </a>
                    </div>
                    
                    <div><button @click="likeMovie(movie.id)"
                    :class="{ liked: movie.isLiked }"
                    class="like-btn d-flex justify-content-center align-items-center">
                    <img v-if="movie.isLiked" src="@/assets/img/button_like.png" alt="" style="height: 20px; margin-right:10px;">
                    <img v-if="!movie.isLiked" src="@/assets/img/button_unlike.png" alt="" style="height: 20px; margin-right:10px;">
                    <span>{{ movie.like_count }}</span>
                    </button></div>
                  </div>
                  <div class="movie-detail-info my-3">
                    <div class="my-1">배우 : {{ getPeoples(movieActors) }}</div>
                    <div class="my-1">감독 : {{ getPeoples(movieDirectors) }}</div>
                    <div class="my-1">제작진 : {{ getPeoples(movieProducers) }}</div>
                  </div>
                </div>
              </div>
            <div class="my-2 movie-detail-content">
              <p>{{ movie.overview }}</p>
              <h1 class="review-start">Review</h1>
              <review-list
              :reviews="movie.reviews"
              ></review-list>
              <!-- {{ movie.reviews }}
              <form action="" @submit.prevent="submitReview">
                <div>
                  <label for="review-title">리뷰 제목</label>
                  <input type="text" name="review-title" v-model="reviewTitle">
                </div>
                <div>
                  <label for="review-content">리뷰 내용</label>
                  <input type="text" name="review-content" v-model="reviewContent">
                </div>
                <div>
                  <label for="review-vote">평점</label>
                  <input type="number" name="review-vote" v-model="reviewVote">
                </div>
                <button>작성</button> -->
              <!-- </form> -->
            </div>
            </div>
          </div>
        </b-modal>
        <movie-card
        v-for="(movie, idx) in movieSort(sortOrder)"
        :key="idx"
        :movie="movie"
        class=""
        @click="movieDetail"
        >
        </movie-card>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import MovieCard from '@/components/MovieCard.vue'
  import ReviewList from '@/components/ReviewList.vue'

  export default {
    name: 'MovieView',
    components: {
      MovieCard,
      ReviewList,
    },
    data: function () {
      return {
        modalShow: false,
        reviewTitle: '',
        reviewContent: '',
        reviewVote: 10,
        sortOrder: "관객수"
      }
    },
    computed: {
      ...mapGetters(['movies', 'movie', 'movieActors', 'movieDirectors', 'movieProducers', 'currentUser']),
      orderedListOptions: function() {
        return {
          "관객수": () => { return this.movies.slice().sort( function(a, b) {
            return b.popularity - a.popularity
          })
          },
          "평점": () => { return this.movies.slice().sort( function(a, b) {
            return b.vote_average - a.vote_average
          }

          ) },
          "좋아요": () => { return this.movies.slice().sort( function(a, b) {
            return b.like_count - a.like_count
          }
          ) },
        }
      },
      isLiked: function () {
        // return this.currentUser.pk in this.movie.like_users
        for (const likeUser in this.movie.like_users) {
          console.log(likeUser)
          if (likeUser == this.currentUser.pk) {
            console.log('like!')
            return true
          }
        }
        return false
      }
    },
    methods: {
      ...mapActions(['fetchMovies', 'fetchMovie', 'createReview', 'likeMovie']),
      movieDetail: function(moviePk) {
        console.log(moviePk)
      },
      checkModal() {
        if (this.$route.params.moviePk) {
          this.fetchMovie(this.$route.params.moviePk)
          this.modalShow = true;

        } else {
          console.log('modal close!')
        }
      },
      imgSrc(imgPath) {
        return 'https://image.tmdb.org/t/p/original' + imgPath
      },
      videoSrc(videoPath) {
        return 'https://www.youtube.com/embed/' + videoPath
      },
      getPlayTime(playTime) {
        return `${parseInt(playTime / 60)}h ${playTime % 60}m`
      },
      getPeoples(peopleArray) {
        if (peopleArray) {
          return peopleArray.join(', ')
        } else {
          return ''
        }
      },
      movieSort: function(sortOrder) {
        return this.orderedListOptions[sortOrder]()
      },
      closeModal: function() {
        console.log('closeModal!')
        this.$router.go(-1)
      },
      netflixSrc: function(path) {
        return 'https://www.netflix.com/title/' + path
      },
      watchaSrc: function(path) {
        return 'https://watcha.com/contents/' + path
      }
    },
    created() {
      console.log('created!')
      // setTimeout(() => {
      //   this.fetchMovie(this.$route.params.moviePk)
      // }, 500)
      if (this.$route.params.moviePk){
        this.fetchMovie(this.$route.params.moviePk)
      }
      this.checkModal();
    },
    watch: {
      $route() {
        this.checkModal();
      },
    }

  }
</script>

<style>
.sort-link {
  text-decoration: none;
  color: white;
  margin-left: 1rem;
  font-size:1.2rem;
  font-family: 'pretendard';
  cursor: pointer;
}
.sort-link:hover {
  color: #E9BA13;
}
.sortActive {
  font-weight: bold;
  color: #E9BA13;
}

.modal-body {
  margin:0px;
  padding: 0rem !important;
  background-color: #111111;
  color: white;
  z-index: 1;
  font-weight: 500;
  letter-spacing: 1px;
}
.modal-img {
  width:100% !important;
  position: absolute;
  top:0;
  left:0;
  opacity: 0.2;
  z-index: -1;
}

.movie-detail-title {
  font-size:2.5rem;
  margin-left:0px;
  font-family: 'Hahmlet';
  font-weight: 600;
}
.movie-detail-content,.movie-detail-info {
  font-family: 'Pretendard';
  font-size: 1.2rem;
  margin: 3px;
}

.movie-detail-vote-average {
  margin-left:0px;
}
.movie-ott-btn {
  background-color: transparent;
  border: 0;
  /* border-radius:10px; */
}
.movie-ott-img {
  /* width:80px; */
  height:35px;
}
.like-btn {
  height: 35px;
  width: 90px;
  background-color: #202020 !important;
  color: white !important;
  border:white 1px solid !important;
  border-radius: 8px;
}

.like-btn {
  cursor:pointer;
  box-shadow: rgba(255, 255, 255, 0.24) 0px 3px 8px;
  transition: 0.3s;
}
.like-btn:hover {
  box-shadow: rgba(255, 255, 255, 0.24) 0px 9px 19px, rgba(255, 255, 255, 0.24) 0px 7px 6px;
  
}

.view-title {
  font-family: 'Hahmlet';
  font-weight: 800;
  margin: 4rem;
}

.review-start {
  margin-top: 5rem;
  border-bottom: 2px solid #E9BA13;
  padding-bottom: 17px;
  letter-spacing: 2px;
  font-family: 'Hahmlet';
  font-weight: 600;
}

</style>