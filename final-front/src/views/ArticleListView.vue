<template>
  <div class="container">
		<div class="d-flex justify-content-between" style="margin: 4rem 0 4rem 4rem;">
			<h1 class="article-h1">커뮤니티</h1>
			<button 
			@click="createArticle"
			class="article-btn me-2">CREATE</button>
			
		</div>
			<table class="table mt-5">
				<thead class="align-middle">
					<tr>
						<th scope="col">#</th>
						<th scope="col">제목</th>
						<th scope="col">게시일</th>
						<th scope="col">댓글 수</th>
						<th scope="col">추천 수</th>
						<th scope="col">작성자</th>
					</tr>
				</thead>
				<tbody>
					<tr scope="row" class="article_list"
					v-for="(article, index) in articles"
					:key="article.pk"
					@click="articleDetail(article.pk)">
						<th class="align-middle" style="opacity: 0.5;">{{ index }}</th>
						<td class="align-middle" style="font-weight: bold; font-size: 1.1rem; letter-spacing: 2px;">{{ article.title }}</td>
						<td class="align-middle">{{ getDate(article.created_at) }}</td>
						<td class="align-middle">{{ article.comment_count }}</td>
						<td class="align-middle">{{ article.like_count }}</td>
						<td class="align-middle article-username">{{ article.user.username }}</td>
					</tr>
				</tbody>
			</table>
	</div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      ...mapActions(['fetchArticles']),
			getDate: function(dateTimeData) {
				return dateTimeData.split('T')[0]
			},
			articleDetail(articlePk) {
				this.$router.push({name: 'article', params: {articlePk: articlePk}})
			},
			createArticle() {
				this.$router.push({name: 'articleCreate'})
			}
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>

.article-h1 {
	letter-spacing: 1px;
}

*
{
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

table {
	background: #111111;
}

thead {
	position: relative;
	font-weight: 500;
	font-size: 1.2rem;
	color: white;
	
}

tbody {
	position: relative;
	border: 10px black;
	color: white;
}

.article-username {
	font-family: 'Pretendard';
	color: #E9BA13;
	transition: 0.5s;
	font-weight: 600;
}

.article_list {
	position: relative;
	left: 0;
	color: white;
	height: 4rem;
	letter-spacing: 1px;
	margin: 4px 0;
	cursor: pointer;
}


/* .article_list:hover {
	left: 10px;
} */

.article_list th, td {
	position: relative;
	padding: 8px;
	z-index: 1;
	transition: 0.3s;
}

.article_list:hover::before {
	transform: scaleX(1);
}


.article_list {
	position: relative;
	left: 0;
	/* margin: 4px 0; */
	/* border-left: 2px solid #999; */
	transition: 0.5s;
	cursor: pointer;
}

.article_list:hover {
color: black;
background: #E9BA13;
}

.article_list:hover > .article-username {
color: black;
}


</style>
