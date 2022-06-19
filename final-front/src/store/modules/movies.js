import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default {
  state: {
    movies: [],
    movie: {},
    reviews: [],
    review: {},
  },
  
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    movieActors: state => {
      if (Object.keys(state.movie).length !== 0)
      {
        return state.movie.actors.map((e) => e.name)
      }
    },
    movieDirectors: state => {
      if (Object.keys(state.movie).length !== 0){
        return state.movie.directors.map((e) => e.name)
      }
    },
    movieProducers: state => {
      if (Object.keys(state.movie).length !== 0) {
        return state.movie.producers.map((e) => e.name)
      }
    },
    reviews: state => state.reviews,
    review: state => state.review,
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_REVIEWS: (state, reviews) => state.reviews = reviews,
    SET_REVIEW: (state, review) => state.review = review,
  },

  actions: {
    fetchMovies({ commit }) {
      /* 영화 목록 가져오기
      GET: movies URL (token)
      성공하면 state.movies에 영화 목록 저장
      */
      axios({
        url: drf.movies.movies(),
        method: 'get',
      })
      .then(res => commit('SET_MOVIES', res.data))
      .catch(err => console.error(err.response))
    },

    fetchMovie({ commit, getters }, moviePk) {
      /* 단일 영화 가져오기
      GET: movie URL (token)
      성공하면 state.movie에 영화 저장
      */
     axios({
       url: drf.movies.movie(moviePk),
       method: 'get',
       headers: getters.authHeader
     })
     .then(res => commit('SET_MOVIE', res.data))
     .catch(err => {
       console.error(err.response)
       if (err.rseponse.status === 404) {
         router.push({ name: 'NotFound404' })
       }
     })
    },

    likeMovie({ commit, getters }, moviePk) {
      /*
      POST: likeMovie URL(token)
      */
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_MOVIE', res.data))
      .catch(err => console.error(err.response))
    },
    createReview({ getters }, { moviePk, review}) {
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
      .then(res => {
        console.log(res.data)
      })
      .catch(err => console.error(err.response))
    },
    updateReview({ getters }, {reviewPk, title, content, vote_average}) {
      const comment = { title, content, vote_average }
      axios({
          url: drf.movies.review(reviewPk),
          method: 'put',
          data: comment,
          headers: getters.authHeader,
      })
      .then(res => {
          console.log(res.data)
      })
      .catch(err => console.error(err.response))
    },
    deleteReview({ getters }, reviewPk) {
      console.log('isDelete?!')
      if (confirm('정말 삭제하시겠습니까?')) {
          axios({
              url: drf.movies.review(reviewPk),
              method: 'delete',
              data: {},
              headers: getters.authHeader,
          })
          .then(res => {
              console.log('review delete completed!', res.data)
            //   const payload = { username: this.state.user }
            // actions.fetchProfile(payload)
          })
          .catch(err => console.error(err.response))
      }
  },
  }
}