export default class Book {
  constructor({id, name, author, description, image, url, category, keywords, updateTime, state, chapters, curChapter, nextChapter, prevChapter}) {
    this.id = id
    this.name = name
    this.author = author
    this.description = description
    this.image = image
    this.url = url
    this.category = category
    this.keywords = keywords
    this.updateTime = updateTime
    this.state = state
    this.chapters = chapters
    this.curChapter = curChapter
    this.nextChapter = nextChapter
    this.prevChapter = prevChapter
  }
}