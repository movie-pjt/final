<template>
  <div id="carousel-div"
  @mousedown="getMouseDown($event)"
  @mousemove="getMouseMove($event)"
  @mouseup="getMouseUp()"
  style="width: 100%"
  >
    <div id="drag-container"
    :style="{transform: 'rotateX(' + (-tY) + 'deg)' + 'rotateY(' + tX + 'deg)'}"
    >
      <div id="spin-container"
      :style="{
        width: imgWidth + 'px',
        height: imgHeight + 'px',
        animation: 'spin 35s infinite linear',
        animationPlayState: spinState
        }">
        <!-- Add your images (or video) here -->
        <img
        v-for="(movie, idx) in topMovies"
        :key="idx"
        :src="imgSrc(movie.poster_path)"
        :style="{
          transform: 'rotateY(' + (idx * (360 / imgCount)) + 'deg) translateZ(' + radius + 'px',
          transitionDelay: delayTime || (imgCount - idx) / 4 + 's'
          }"
        @mouseover="carouselStop"
        @mouseleave="carouselRotate"
        @click="movieDetail(movie.id)"
        style="-webkit-user-drag: none;"
        alt=""
        class="carousel-movie-img"
        >
        <!-- <p>Jang & Hong</p> -->
        <p>
          <img src="@/assets/img/logo3.png" alt="" style="width: 400px">
        </p>
      </div>
      <div id="ground" :style="{ width: radius * 3 + 'px', height: radius * 3 + 'px' }"
      ></div>
    </div>

    <div id="music-container" style="display: hidden;"></div>
  </div>
</template>

<script>
// import '@/assets/carousel.js'
// import '@/assets/carousel.css'
import router from '@/router'

export default {
  name: 'MovieCarousel',
  props: {
    topMovies: Array,
  },
  data: function () {
    return {
      radius: 320,
      autoRotate: true,
      rotateSpeed: -60,
      imgWidth: 170,
      imgHeight: 240,
      imgCount: 8,
      delayTime: 1,
      desX: 0,
      desY: 0,
      tX: 0,
      tY: 8,
      spinAnimation: `'spin' ${Math.abs(this.rotateSpeed)}s infinite linear`,
      spinState: 'running',
      isDrag: false,
      sX: 0,
    }
  },
  computed: {

  },
  methods: {
    init: function (delayTime) {
      for (let i = 0; i < this.imgCount; i++) {
        console.log(i, delayTime)
      }
    },
    applyTransform: function(obj) {
      console.log(obj)
    },
    carouselStop: function() {
      // console.log('stop')
      this.spinState = 'paused'
    },
    carouselRotate: function() {
      // console.log('rotate')
      this.spinState = 'running'
    },
    rotate: function () {
      var animationName = (this.rotateSpeed > 0 ? 'spin' : 'spinRevert')
      this.spinAnimation = `${animationName} ${Math.abs(this.rotateSpeed)}s infinite linear`
    },
    movieDetail: function (movie_pk) {
      // router.push({name: 'movies'})
      // console.log('carousel', movie_pk)
      router.push({ name: 'movie_detail', params:{ moviePk: movie_pk } })
    },
    imgSrc(imgPath) {
        return 'https://image.tmdb.org/t/p/original' + imgPath
    },
    getMouseDown(e) {
      // console.log('MouseDown!!', e.clientX)
      this.isDrag = true
      this.sX = e.clientX
      // console.log(e)
      // let sX = e.clientX;
      // console.log(this.event)
    },
    getMouseMove(e) {
      if (this.isDrag){
        // console.log('mouseMove!!!', e.clientX)
        let nX = e.clientX;
        this.desX = nX - this.sX
        this.tX += this.desX * 0.15
        this.applyTransform
        this.sX = nX
      }
    },
    getMouseUp() {
      this.isDrag = false
      // console.log('MouseUp!!', e.clientX)
    }
  },
  created () {
    this.rotate
  }
}
</script>

<style>
  * {
  margin: 0;
  padding: 0;
}

#carousel-div {
  height: 800px;
  /* for touch screen */
  touch-action: none; 
  position: absolute;
  top:10%;
  left:50%;
  transform: translate(-50%, 0%);
  width:1000px;
  z-index: -1;
  -webkit-user-select:none;
  -moz-user-select:none;
  -ms-user-select:none;
  user-select:none
}

#carousel-div {
  overflow: hidden;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  background: #111111;
  -webkit-perspective: 1000px;
          perspective: 1000px;
  -webkit-transform-style: preserve-3d;
          transform-style: preserve-3d;
}

#drag-container, #spin-container {
  /* position: relative; */
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  margin: auto;
  -webkit-transform-style: preserve-3d;
          transform-style: preserve-3d;
  -webkit-transform: rotateX(-10deg);
          transform: rotateX(-10deg);
}

#drag-container .carousel-movie-img {
  -webkit-transform-style: preserve-3d;
          transform-style: preserve-3d;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  line-height: 200px;
  font-size: 50px;
  text-align: center;
  -webkit-box-shadow: 0 0 8px #fff;
          box-shadow: 0 0 8px #fff;
  -webkit-box-reflect: below 10px linear-gradient(transparent, transparent, #0005);
}

#drag-container .carousel-movie-img:hover {
  -webkit-box-shadow: 0 0 15px #fffd;
          box-shadow: 0 0 15px #fffd;
  -webkit-box-reflect: below 10px linear-gradient(transparent, transparent, #0007);
  cursor: pointer;
}

#drag-container p {
  font-family: Serif;
  position: absolute;
  top: 100%;
  left: 50%;
  -webkit-transform: translate(-50%,-50%) rotateX(90deg);
          transform: translate(-50%,-50%) rotateX(90deg);
  color: #fff;
}

#ground {
  width: 1200px;
  height: 1200px;
  position: absolute;
  top: 100%;
  left: 50%;
  -webkit-transform: translate(-50%,-50%) rotateX(90deg);
          transform: translate(-50%,-50%) rotateX(90deg);
  background: -webkit-radial-gradient(center center, farthest-side , #9993, transparent);
}

@-webkit-keyframes spin {
  from{
    -webkit-transform: rotateY(0deg);
            transform: rotateY(0deg);
  } to{
    -webkit-transform: rotateY(360deg);
            transform: rotateY(360deg);
  }
}

@keyframes spin {
  from{
    -webkit-transform: rotateY(0deg);
            transform: rotateY(0deg);
  } to{
    -webkit-transform: rotateY(360deg);
            transform: rotateY(360deg);
  }
}
@-webkit-keyframes spinRevert {
  from{
    -webkit-transform: rotateY(360deg);
            transform: rotateY(360deg);
  } to{
    -webkit-transform: rotateY(0deg);
            transform: rotateY(0deg);
  }
}
@keyframes spinRevert {
  from{
    -webkit-transform: rotateY(360deg);
            transform: rotateY(360deg);
  } to{
    -webkit-transform: rotateY(0deg);
            transform: rotateY(0deg);
  }
}

.carousel-img {
  -webkit-transform-style: preserve-3d;
          transform-style: preserve-3d;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  line-height: 200px;
  font-size: 50px;
  text-align: center;
  -webkit-box-shadow: 0 0 8px #fff;
          box-shadow: 0 0 8px #fff;
  -webkit-box-reflect: below 10px linear-gradient(transparent, transparent, #0005);
}
</style>