//
// AdditionalPropertiesClass.swift
//
// Generated by openapi-generator
// https://openapi-generator.tech
//

import Foundation

@available(*, deprecated, renamed: "PetstoreClientAPI.AdditionalPropertiesClass")
public typealias AdditionalPropertiesClass = PetstoreClientAPI.AdditionalPropertiesClass

extension PetstoreClientAPI {

public final class AdditionalPropertiesClass: @unchecked Sendable, Codable, ParameterConvertible, Hashable {

    public private(set) var mapString: [String: String]?
    public private(set) var mapMapString: [String: [String: String]]?

    public init(mapString: [String: String]? = nil, mapMapString: [String: [String: String]]? = nil) {
        self.mapString = mapString
        self.mapMapString = mapMapString
    }

    public enum CodingKeys: String, CodingKey, CaseIterable {
        case mapString = "map_string"
        case mapMapString = "map_map_string"
    }

    // Encodable protocol methods

    public func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encodeIfPresent(mapString, forKey: .mapString)
        try container.encodeIfPresent(mapMapString, forKey: .mapMapString)
    }

    public static func == (lhs: AdditionalPropertiesClass, rhs: AdditionalPropertiesClass) -> Bool {
        lhs.mapString == rhs.mapString &&
        lhs.mapMapString == rhs.mapMapString
        
    }

    public func hash(into hasher: inout Hasher) {
        hasher.combine(mapString?.hashValue)
        hasher.combine(mapMapString?.hashValue)
        
    }
}

}
