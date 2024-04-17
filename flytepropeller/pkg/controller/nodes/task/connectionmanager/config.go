package connectionmanager

import "github.com/flyteorg/flyte/flytestdlib/config"

//go:generate pflags Config --default-var defaultConfig

const SectionKey = "connections"

var (
	defaultConfig = &Config{}

	section = config.MustRegisterSection(SectionKey, defaultConfig)
)

type Connection struct {
	Secrets map[string]string `json:"secrets" pflag:", secrets to be used by the task"`
	Configs map[string]string `json:"configs" pflag:", configs to be used by the task"`
}

type Config struct {
	Connection map[string]Connection `json:"connection" pflag:", the connection that saves the secrets and configs"`
}

func GetConfig() *Config {
	return section.GetConfig().(*Config)
}