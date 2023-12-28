package com.cms.entities;

import java.time.LocalDateTime;
import java.util.List;

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
@Setter
@Getter
@NoArgsConstructor
@Entity
@ToString
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
	
	
	
}
