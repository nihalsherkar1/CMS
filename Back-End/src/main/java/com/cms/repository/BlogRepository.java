package com.cms.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.cms.entities.Blogs;

@Repository
public interface BlogRepository extends JpaRepository<Blogs, Long> {
 
	public Blogs findBlgById(Long id);
	 
}
