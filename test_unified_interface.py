#!/usr/bin/env python3
"""Test unified interface implementation for docling-analysis-framework."""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import docling_analysis_framework as daf

def test_unified_interface():
    """Test all required interface methods."""
    
    print("Testing docling-analysis-framework unified interface...")
    
    # Find a test file
    test_files = [
        "../general_files/small/pdf/sample1.pdf",
        "../general_files/small/pdf/sample2.pdf",
        "../general_files/small/pdf/sample3.pdf",
        "../general_files/small/txt/sample1.txt",
        "../tests/test_invoice.pdf",
        "../downloader/artifacts/analysis_results/test_invoice.pdf"
    ]
    
    test_file = None
    for file_path in test_files:
        if os.path.exists(file_path):
            test_file = file_path
            break
    
    if not test_file:
        print("⚠️  No test file found, creating minimal test...")
        # Create a minimal test file
        test_file = "test_doc.txt"
        with open(test_file, 'w') as f:
            f.write("This is a test document for unified interface testing.")
    
    try:
        # Test with the unified interface
        print(f"\n📄 Testing with file: {test_file}")
        result = daf.analyze_unified(test_file)
        
        print("\n✅ Basic instantiation successful")
        
        # Test required properties
        print("\n📋 Testing required properties:")
        print(f"  document_type: {result.document_type}")
        print(f"  confidence: {result.confidence}")
        print(f"  metadata: {result.metadata}")
        print(f"  content preview: {result.content[:100]}..." if result.content else "  content: (empty)")
        print(f"  ai_opportunities: {result.ai_opportunities[:2]}..." if result.ai_opportunities else "  ai_opportunities: []")
        print(f"  framework: {result.framework}")
        
        # Test dictionary access
        print("\n🔍 Testing dictionary access:")
        assert result['document_type'] == result.document_type, "Dict access doesn't match attribute"
        assert result['framework'] == 'docling-analysis-framework', "Framework name mismatch"
        print("  result['document_type'] ✓")
        print("  result['framework'] ✓")
        
        # Test dict methods
        print("\n📚 Testing dict methods:")
        assert 'document_type' in result, "'in' operator failed"
        print("  'document_type' in result ✓")
        
        assert result.get('missing', 'default') == 'default', "get() with default failed"
        print("  result.get('missing', 'default') ✓")
        
        assert isinstance(list(result.keys()), list), "keys() failed"
        print("  result.keys() ✓")
        
        assert isinstance(list(result.values()), list), "values() failed"
        print("  result.values() ✓")
        
        assert isinstance(list(result.items()), list), "items() failed"
        print("  result.items() ✓")
        
        # Test conversion
        print("\n🔄 Testing conversion:")
        as_dict = result.to_dict()
        assert isinstance(as_dict, dict), "to_dict() didn't return dict"
        assert 'document_type' in as_dict, "Required field missing in dict"
        assert 'raw_analysis' in as_dict, "Raw analysis missing in dict"
        print("  result.to_dict() ✓")
        
        # Test access to original fields
        print("\n🔗 Testing access to original fields:")
        if hasattr(result, 'file_path'):
            print(f"  result.file_path: {result.file_path} ✓")
        if hasattr(result, 'handler_used'):
            print(f"  result.handler_used: {result.handler_used} ✓")
        
        print("\n✅ All tests passed!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        # Clean up test file if we created it
        if test_file == "test_doc.txt" and os.path.exists(test_file):
            os.remove(test_file)
    
    return True

if __name__ == "__main__":
    success = test_unified_interface()
    sys.exit(0 if success else 1) 