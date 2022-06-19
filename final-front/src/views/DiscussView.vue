<template>
  <div class="container">
    <h1 class="discuss-h1 text-start">토론 / 논쟁</h1>
    <div class="container"
      >
      <div class="row">
        <div class="discuss-card d-flex px-0"
        v-for="discuss in discusses"
        :key="discuss.pk"
        @click="discussDetail(discuss.pk)"
        >
          <div class="col-md-4 col-12">
            <img :src="imgSrc(discuss.img)"
                class="img-fluid rounded-start img-space" alt="이미지가 없어요.">
          </div>
          <div class="discuss-body col-md-8 col-0">
              <div class="text-start d-flex flex-column justify-content-between px-3 py-3" style="height: 100%">
                <h5 class="mt-2 disuss-title" style="font-weight: bold; font-size: 35px; font-family: 'Hahmlet'">{{ discuss.title }}</h5>
                <div class="d-flex flex-column my-2" style="font-size: 25px">
                  <div class="d-flex align-items-center">
                    <img src="@/assets/img/rose_red.png" alt="" width="35px">
                    <span class="ms-2">
                      {{ getContentA(discuss.content) }}
                    </span>
                  </div>
                  <div class="text-center">VS</div>
                  <div class="d-flex align-items-center justify-content-end">
                    <span class="me-2">
                      {{ getContentB(discuss.content) }}
                    </span>
                    <img src="@/assets/img/rose_blue.png" alt="" width="32px">
                  </div>
                </div>
                <div class="d-flex col-md-4 mx-3 my-2 justify-content-between align-items-center ">
                  <div class="d-flex align-items-center me-3">
                    <font-awesome-icon class="fa-2x" icon="fa-solid fa-comment" />
                    <span class="mx-3 discuss-count">{{ discuss.discuss_comment_count }}</span>
                  </div>
                  <div class="d-flex align-items-center me-3">
                    <img src="@/assets/img/rose_red.png" alt="" width="35px">
                    <span class="mx-3 discuss-count">{{ discuss.choice_a_count }}</span>
                  </div>
                  <div class="d-flex align-items-center me-3">
                    <img src="@/assets/img/rose_blue.png" alt="" width="32px">
                    <span class="mx-3 discuss-count">{{ discuss.choice_b_count }}</span>
                  </div>
                </div>
              </div>
            </div>
        </div>
      </div>
    </div>
	</div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'discussView',
    computed: {
      ...mapGetters(['discusses'])
    },
    methods: {
      ...mapActions(['fetchdiscusses']),
			discussDetail(discussPk) {
        console.log('discussDetail')
        console.log(discussPk)
				this.$router.push({name: 'discussDetail', params: {discussPk: discussPk}})
			},
      imgSrc(imgPath) {
        return imgPath
      },
      getContentA: function(text) {
				return text.split('vs')[0]
			},
      getContentB: function(text) {
				return text.split('vs')[1]
			},
    },
    created() {
      this.fetchdiscusses()
    },
  }
</script>

<style>

.discuss-h1 {
  margin: 4rem;
  
}

.img-space {
  width: 30rem;
  /* height: 16rem; */
  height: 100% !important;
  object-fit: cover !important;
}


.discuss-card:hover {
	/* left: 10px; */
  transform: translateY(-10px);
  box-shadow: rgba(255, 255, 255, 0.54) 0px 9px 20px;
}

.discuss-card:hover::before {
	transform: scaleX(1);
}

.discuss-card {
  position: relative;
  height: 18rem;
  color: white;
  background: #111111 !important;
  border: 2px solid white !important;
  margin: 2rem;
  transition: 0.3s;
	cursor: pointer;
  border-radius: 10px;
}

.discuss-card h5 {
  color:#E9BA13;
  transition: 1s;
  
}

.discuss-body {
  font-family: 'Pretendard';
}

.discuss-body:hover {
left: 10px;
color: black;
/* background: #E9BA13; */
background: rgba(227, 213, 16, 0.954);
transition: 1s;
}

.discuss-body:hover h5 {
left: 10px;
color: black;
transition: 1s;
}

.discuss-count {
  font-size: 1.3rem;
  font-weight: 700;
}
</style>
