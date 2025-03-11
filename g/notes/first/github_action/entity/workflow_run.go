package entity

import "gorm.io/gorm"

// WorkflowRun GitHub Actions 워크플로우 실행 상태
type WorkflowRun struct {
	gorm.Model
	ID         int    `json:"id" gorm:"primaryKey"`
	Name       string `json:"name"`
	Status     string `json:"status"`
	Conclusion string `json:"conclusion"`
	CreatedAt  string `json:"created_at"`
	RepoURL    string `json:"repo_url"`
}
