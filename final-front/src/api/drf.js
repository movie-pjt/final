const HOST = 'http://localhost:8000/api/v1/'

const MOVIES = 'movies/'
const ARTICLES = 'articles/'
const DISCUSS = 'discuss/'
const ACCOUNTS = 'accounts/'
const COMMENTS = 'comments/'
const REVIEWS = 'reviews/'
const LIKES = 'like/'
const RECOMMENDATIONS = 'recommendations/'

export default {
  movies: {
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    review: reviewPk => HOST + MOVIES + REVIEWS + `${reviewPk}/`,
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + LIKES,
    likeReview: reviewPk => HOST + MOVIES + REVIEWS + `${reviewPk}/` + LIKES,
    movieCount: moviePk => HOST + MOVIES + `${moviePk}/` + 'movie_count/',
    recommendations: () => HOST + MOVIES + RECOMMENDATIONS,
  },
  articles: {
    articles: () => HOST + ARTICLES,
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + LIKES,
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,

  },
  discuss: {
    discusses: () => HOST + DISCUSS,
    discuss: discussPk => HOST + DISCUSS + `${discussPk}`,
    discussChoiceA: discussPk => HOST + DISCUSS + `${discussPk}/` + 'choice_a/',
    discussChoiceB: discussPk => HOST + DISCUSS + `${discussPk}/` + 'choice_b/',
    discussComments: discussPk => HOST + DISCUSS + `${discussPk}/` + COMMENTS,
    discussComment: (discussPk, commentPk) => HOST + DISCUSS + `${discussPk}/` + COMMENTS + `${commentPk}/`,
  },
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
}