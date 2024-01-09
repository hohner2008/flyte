// Code generated by "enumer --type=TemplateScheme --trimprefix=TemplateScheme -json -yaml"; DO NOT EDIT.

package tasklog

import (
	"encoding/json"
	"fmt"
)

const _TemplateSchemeName = "PodTaskExecutionFlyin"

var _TemplateSchemeIndex = [...]uint8{0, 3, 16, 21}

func (i TemplateScheme) String() string {
	if i < 0 || i >= TemplateScheme(len(_TemplateSchemeIndex)-1) {
		return fmt.Sprintf("TemplateScheme(%d)", i)
	}
	return _TemplateSchemeName[_TemplateSchemeIndex[i]:_TemplateSchemeIndex[i+1]]
}

var _TemplateSchemeValues = []TemplateScheme{0, 1, 2}

var _TemplateSchemeNameToValueMap = map[string]TemplateScheme{
	_TemplateSchemeName[0:3]:   0,
	_TemplateSchemeName[3:16]:  1,
	_TemplateSchemeName[16:21]: 2,
}

// TemplateSchemeString retrieves an enum value from the enum constants string name.
// Throws an error if the param is not part of the enum.
func TemplateSchemeString(s string) (TemplateScheme, error) {
	if val, ok := _TemplateSchemeNameToValueMap[s]; ok {
		return val, nil
	}
	return 0, fmt.Errorf("%s does not belong to TemplateScheme values", s)
}

// TemplateSchemeValues returns all values of the enum
func TemplateSchemeValues() []TemplateScheme {
	return _TemplateSchemeValues
}

// IsATemplateScheme returns "true" if the value is listed in the enum definition. "false" otherwise
func (i TemplateScheme) IsATemplateScheme() bool {
	for _, v := range _TemplateSchemeValues {
		if i == v {
			return true
		}
	}
	return false
}

// MarshalJSON implements the json.Marshaler interface for TemplateScheme
func (i TemplateScheme) MarshalJSON() ([]byte, error) {
	return json.Marshal(i.String())
}

// UnmarshalJSON implements the json.Unmarshaler interface for TemplateScheme
func (i *TemplateScheme) UnmarshalJSON(data []byte) error {
	var s string
	if err := json.Unmarshal(data, &s); err != nil {
		return fmt.Errorf("TemplateScheme should be a string, got %s", data)
	}

	var err error
	*i, err = TemplateSchemeString(s)
	return err
}

// MarshalYAML implements a YAML Marshaler for TemplateScheme
func (i TemplateScheme) MarshalYAML() (interface{}, error) {
	return i.String(), nil
}

// UnmarshalYAML implements a YAML Unmarshaler for TemplateScheme
func (i *TemplateScheme) UnmarshalYAML(unmarshal func(interface{}) error) error {
	var s string
	if err := unmarshal(&s); err != nil {
		return err
	}

	var err error
	*i, err = TemplateSchemeString(s)
	return err
}