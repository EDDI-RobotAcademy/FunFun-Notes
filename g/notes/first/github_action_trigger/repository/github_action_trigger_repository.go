package repository

type GitHubActionTriggerRepository interface {
	FetchTriggers(repoUrl string, token string) ([]string, error)
}
