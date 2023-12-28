package com.cms.entities;

import java.util.List;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Data
@Entity
@NoArgsConstructor
@ToString
public class Users {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	@Column(name = "name")
	private String name;
	
	@Column(name = "email")
	private String email;

	@Column(name = "password")
	private String password;
	
	@Column(name = "image")
	private String image;
	
	@OneToMany(cascade = CascadeType.ALL,mappedBy = "userId")
	private List<Blogs> blog;
	
	
	@OneToMany(mappedBy = "user",cascade = CascadeType.ALL)
	private List<Likes> like;
	
	
	
	public Users() {
		super();
		 
	}



	public Users(Long id, String name, String email, String password, String image) {
		super();
		this.id = id;
		this.name = name;
		this.email = email;
		this.password = password;
		this.image = image;
	}



	public Long getId() {
		return id;
	}



	public void setId(Long id) {
		this.id = id;
	}



	public String getName() {
		return name;
	}



	public void setName(String name) {
		this.name = name;
	}



	public String getEmail() {
		return email;
	}



	public void setEmail(String email) {
		this.email = email;
	}



	public String getPassword() {
		return password;
	}



	public void setPassword(String password) {
		this.password = password;
	}



	public String getImage() {
		return image;
	}



	public void setImage(String image) {
		this.image = image;
	}



	public List<Blogs> getBlog() {
		return blog;
	}



	public void setBlog(List<Blogs> blog) {
		this.blog = blog;
	}



	public List<Likes> getLike() {
		return like;
	}



	public void setLike(List<Likes> like) {
		this.like = like;
	}
	
	
	
	
	
	 
	
	
}
