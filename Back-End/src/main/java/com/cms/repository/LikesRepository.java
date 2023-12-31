package com.cms.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.cms.entities.Likes;

@Repository
public interface LikesRepository extends JpaRepository<Likes, Long> {

}
