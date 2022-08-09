// Code generated by go generate; DO NOT EDIT.
// This file was generated by robots.

package admin

import (
	"encoding/json"
	"reflect"

	"fmt"

	"github.com/spf13/pflag"
)

// If v is a pointer, it will get its element value or the zero value of the element type.
// If v is not a pointer, it will return it as is.
func (Config) elemValueOrNil(v interface{}) interface{} {
	if t := reflect.TypeOf(v); t.Kind() == reflect.Ptr {
		if reflect.ValueOf(v).IsNil() {
			return reflect.Zero(t.Elem()).Interface()
		} else {
			return reflect.ValueOf(v).Interface()
		}
	} else if v == nil {
		return reflect.Zero(t).Interface()
	}

	return v
}

func (Config) mustJsonMarshal(v interface{}) string {
	raw, err := json.Marshal(v)
	if err != nil {
		panic(err)
	}

	return string(raw)
}

func (Config) mustMarshalJSON(v json.Marshaler) string {
	raw, err := v.MarshalJSON()
	if err != nil {
		panic(err)
	}

	return string(raw)
}

// GetPFlagSet will return strongly types pflags for all fields in Config and its nested types. The format of the
// flags is json-name.json-sub-name... etc.
func (cfg Config) GetPFlagSet(prefix string) *pflag.FlagSet {
	cmdFlags := pflag.NewFlagSet("Config", pflag.ExitOnError)
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "endpoint"), defaultConfig.Endpoint.String(), "For admin types,  specify where the uri of the service is located.")
	cmdFlags.Bool(fmt.Sprintf("%v%v", prefix, "insecure"), defaultConfig.UseInsecureConnection, "Use insecure connection.")
	cmdFlags.Bool(fmt.Sprintf("%v%v", prefix, "insecureSkipVerify"), defaultConfig.InsecureSkipVerify, "InsecureSkipVerify controls whether a client verifies the server's certificate chain and host name. Caution : shouldn't be use for production usecases'")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "caCertFilePath"), defaultConfig.CACertFilePath, "Use specified certificate file to verify the admin server peer.")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "maxBackoffDelay"), defaultConfig.MaxBackoffDelay.String(), "Max delay for grpc backoff")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "perRetryTimeout"), defaultConfig.PerRetryTimeout.String(), "gRPC per retry timeout")
	cmdFlags.Int(fmt.Sprintf("%v%v", prefix, "maxRetries"), defaultConfig.MaxRetries, "Max number of gRPC retries")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "authType"), defaultConfig.AuthType.String(), "Type of OAuth2 flow used for communicating with admin.ClientSecret, Pkce, ExternalCommand are valid values")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "tokenRefreshWindow"), defaultConfig.TokenRefreshWindow.String(), "Max duration between token refresh attempt and token expiry.")
	cmdFlags.Bool(fmt.Sprintf("%v%v", prefix, "useAuth"), defaultConfig.DeprecatedUseAuth, "Deprecated: Auth will be enabled/disabled based on admin's dynamically discovered information.")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "clientId"), defaultConfig.ClientID, "Client ID")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "clientSecretLocation"), defaultConfig.ClientSecretLocation, "File containing the client secret")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "clientSecretEnvVar"), defaultConfig.ClientSecretEnvVar, "Environment variable containing the client secret")
	cmdFlags.StringSlice(fmt.Sprintf("%v%v", prefix, "scopes"), defaultConfig.Scopes, "List of scopes to request")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "authorizationServerUrl"), defaultConfig.DeprecatedAuthorizationServerURL, "This is the URL to your IdP's authorization server. It'll default to Endpoint")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "tokenUrl"), defaultConfig.TokenURL, "OPTIONAL: Your IdP's token endpoint. It'll be discovered from flyte admin's OAuth Metadata endpoint if not provided.")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "authorizationHeader"), defaultConfig.DeprecatedAuthorizationHeader, "Custom metadata header to pass JWT")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "pkceConfig.timeout"), defaultConfig.PkceConfig.BrowserSessionTimeout.String(), "")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "pkceConfig.refreshTime"), defaultConfig.PkceConfig.TokenRefreshGracePeriod.String(), "")
	cmdFlags.StringSlice(fmt.Sprintf("%v%v", prefix, "command"), defaultConfig.Command, "Command for external authentication token generation")
	cmdFlags.String(fmt.Sprintf("%v%v", prefix, "defaultServiceConfig"), defaultConfig.DefaultServiceConfig, "")
	return cmdFlags
}
