package com.cms.entities;

import java.time.LocalDateTime;
import java.util.List;

import org.springframework.stereotype.Component;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Data
@Entity
@ToString
@Component
public class Blogs {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	@Column
	private String title;
	
	@Column
	private String author;
	
	@Column
	private LocalDateTime updatedTimestamp;
	
	@Column(columnDefinition = "MEDIUMTEXT")
	private String content;
	
	@Column
	private String category;
	
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name = "user_id")
	private Users userId;

	
	@OneToMany(mappedBy="blog")
	private List<Likes> like;
	
	
	 
	
	public Blogs(Long id, String title, String author, LocalDateTime updatedTimestamp, String content, String category,
			Users userId) {
		super();
		this.id = id;
		this.title = title;
		this.author = author;
		this.updatedTimestamp = updatedTimestamp;
		this.content = content;
		this.category = category;
		this.userId = userId;
	}




	public Blogs() {
		super();
	 
	}




	public Long getId() {
		return id;
	}




	public void setId(Long id) {
		this.id = id;
	}




	public String getTitle() {
		return title;
	}




	public void setTitle(String title) {
		this.title = title;
	}




	public String getAuthor() {
		return author;
	}




	public void setAuthor(String author) {
		this.author = author;
	}




	public LocalDateTime getUpdatedTimestamp() {
		return updatedTimestamp;
	}




	public void setUpdatedTimestamp(LocalDateTime updatedTimestamp) {
		this.updatedTimestamp = updatedTimestamp;
	}




	public String getContent() {
		return content;
	}




	public void setContent(String content) {
		this.content = content;
	}




	public String getCategory() {
		return category;
	}




	public void setCategory(String category) {
		this.category = category;
	}




	public Users getUserId() {
		return userId;
	}




	public void setUserId(Users userId) {
		this.userId = userId;
	}




	public List<Likes> getLike() {
		return like;
	}




	public void setLike(List<Likes> like) {
		this.like = like;
	}




	@Override
	public String toString() {
		return "Blogs [id=" + id + ", title=" + title + ", author=" + author + ", updatedTimestamp=" + updatedTimestamp
				+ ", content=" + content + ", category=" + category + ", userId=" + userId + ", like=" + like + "]";
	}
	
	
	
}
