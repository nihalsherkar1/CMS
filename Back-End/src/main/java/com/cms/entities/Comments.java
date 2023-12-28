package com.cms.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
 
@Entity
@Setter
@Getter
@NoArgsConstructor
@ToString
public class Comments {

	@Id @GeneratedValue(strategy = GenerationType.IDENTITY) 
	private Long id;
	
	@Column 
	private String comment;
	
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="blog_id")
	private Blogs blog;
	
	@ManyToOne(fetch = FetchType.LAZY)
	@JoinColumn(name="user_id")
	private Users user;

	public Comments(Long id, String comment, Blogs blog, Users user) {
		super();
		this.id = id;
		this.comment = comment;
		this.blog = blog;
		this.user = user;
	}

	 
	
	
}
